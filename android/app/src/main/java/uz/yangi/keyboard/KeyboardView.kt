package uz.yangi.keyboard

import android.annotation.SuppressLint
import android.content.Context
import android.graphics.drawable.GradientDrawable
import android.os.Handler
import android.os.Looper
import android.view.Gravity
import android.view.HapticFeedbackConstants
import android.view.MotionEvent
import android.view.View
import android.widget.FrameLayout
import android.widget.LinearLayout
import android.widget.TextView
import java.util.Locale

interface KeyListener {
    fun onText(text: String)
    fun onDelete()
    fun onEnter()
    fun onGlobe(showPicker: Boolean)
}

@SuppressLint("ViewConstructor", "ClickableViewAccessibility")
class KeyboardView(
    context: Context,
    private val layout: MobileLayout,
    private val listener: KeyListener,
) : FrameLayout(context) {

    private enum class Shift { OFF, ONCE, LOCKED }

    private val rows = LinearLayout(context).apply { orientation = LinearLayout.VERTICAL }
    private val letterKeys = mutableListOf<Pair<TextView, String>>()
    private val handler = Handler(Looper.getMainLooper())
    private var shiftKey: TextView? = null
    private var popup: View? = null
    private var shift = Shift.OFF
    private var lastShiftTap = 0L

    init {
        setBackgroundColor(context.getColor(R.color.keyboard_bg))
        rows.setPadding(dp(3), dp(4), dp(3), dp(4))
        addView(rows, LayoutParams(LayoutParams.MATCH_PARENT, LayoutParams.WRAP_CONTENT))
        showLayer("letters")
    }

    fun reset() {
        shift = Shift.OFF
        showLayer("letters")
    }

    /** Matn maydoni bosh harf kutayotganini bildiradi (gap boshi va h.k.). */
    fun setAutoShift(on: Boolean) {
        if (shift == Shift.LOCKED) return
        shift = if (on) Shift.ONCE else Shift.OFF
        refreshLabels()
    }

    override fun onDetachedFromWindow() {
        handler.removeCallbacksAndMessages(null)
        super.onDetachedFromWindow()
    }

    private fun showLayer(name: String) {
        dismissPopup()
        rows.removeAllViews()
        letterKeys.clear()
        shiftKey = null
        for (row in layout.layers.getValue(name)) {
            val line = LinearLayout(context)
            for (key in row) {
                val params = LinearLayout.LayoutParams(0, dp(48), weight(key))
                params.setMargins(dp(3), dp(4), dp(3), dp(4))
                line.addView(makeKey(key), params)
            }
            rows.addView(line)
        }
        refreshLabels()
    }

    private fun makeKey(key: String): TextView {
        val special = isSpecial(key)
        val view = TextView(context).apply {
            gravity = Gravity.CENTER
            textSize = if (special) 16f else 22f
            setTextColor(context.getColor(R.color.key_text))
            background = GradientDrawable().apply {
                cornerRadius = dp(6).toFloat()
                setColor(context.getColor(if (special) R.color.key_special_bg else R.color.key_bg))
            }
            text = label(key)
        }
        when (key) {
            "{shift}" -> {
                shiftKey = view
                view.setOnClickListener { press(it); tapShift() }
            }
            "{del}" -> repeatOnHold(view) { listener.onDelete() }
            "{enter}" -> view.setOnClickListener { press(it); listener.onEnter() }
            "{space}" -> view.setOnClickListener { press(it); type(" ") }
            "{globe}" -> {
                view.setOnClickListener { press(it); listener.onGlobe(false) }
                view.setOnLongClickListener { listener.onGlobe(true); true }
            }
            "{letters}", "{numbers}", "{symbols}" ->
                view.setOnClickListener { press(it); showLayer(key.trim('{', '}')) }
            else -> {
                if (key.any { it.isLetter() }) letterKeys += view to key
                view.setOnClickListener { press(it); type(cased(key)) }
                layout.longPress[key]?.let { alts ->
                    view.setOnLongClickListener { showAlternates(it, alts.map(this::cased)); true }
                }
            }
        }
        return view
    }

    private fun label(key: String) = when (key) {
        "{shift}" -> "⇧"
        "{del}" -> "⌫"
        "{enter}" -> "↵"
        "{space}" -> context.getString(R.string.space_label)
        "{globe}" -> "🌐"
        "{letters}" -> "ABC"
        "{numbers}" -> "123"
        "{symbols}" -> "#+="
        else -> key
    }

    private fun weight(key: String) = when (key) {
        "{space}" -> 4f
        "{enter}" -> 2f
        "{shift}", "{del}", "{letters}", "{numbers}", "{symbols}" -> 1.5f
        else -> 1f
    }

    private fun isSpecial(key: String) = key.length > 1 && key.startsWith("{")

    // Locale.ROOT: turkcha locale'da i -> İ bo'lib qolmasligi uchun.
    private fun cased(text: String) = if (shift == Shift.OFF) text else text.uppercase(Locale.ROOT)

    private fun type(text: String) {
        listener.onText(text)
        if (shift == Shift.ONCE) {
            shift = Shift.OFF
            refreshLabels()
        }
    }

    private fun tapShift() {
        val now = System.currentTimeMillis()
        shift = when {
            shift == Shift.LOCKED -> Shift.OFF
            now - lastShiftTap < 300 -> Shift.LOCKED
            shift == Shift.ONCE -> Shift.OFF
            else -> Shift.ONCE
        }
        lastShiftTap = now
        refreshLabels()
    }

    private fun refreshLabels() {
        for ((view, key) in letterKeys) view.text = cased(key)
        shiftKey?.let {
            it.text = if (shift == Shift.LOCKED) "⇪" else "⇧"
            val color = if (shift == Shift.OFF) R.color.key_special_bg else R.color.key_bg
            (it.background as GradientDrawable).setColor(context.getColor(color))
        }
    }

    private fun repeatOnHold(view: View, action: () -> Unit) {
        val repeat = object : Runnable {
            override fun run() {
                action()
                handler.postDelayed(this, 50)
            }
        }
        view.setOnTouchListener { v, event ->
            when (event.actionMasked) {
                MotionEvent.ACTION_DOWN -> {
                    press(v)
                    action()
                    handler.postDelayed(repeat, 400)
                }
                MotionEvent.ACTION_UP, MotionEvent.ACTION_CANCEL -> handler.removeCallbacks(repeat)
            }
            true
        }
    }

    /** Uzoq bosish: bitta muqobil bo'lsa darhol yoziladi, bir nechta bo'lsa tanlash paneli chiqadi. */
    private fun showAlternates(anchor: View, options: List<String>) {
        press(anchor)
        if (options.size == 1) {
            type(options[0])
            return
        }
        val bar = LinearLayout(context).apply {
            background = GradientDrawable().apply {
                cornerRadius = dp(8).toFloat()
                setColor(context.getColor(R.color.key_special_bg))
            }
            elevation = dp(4).toFloat()
        }
        for (option in options) {
            bar.addView(TextView(context).apply {
                text = option
                gravity = Gravity.CENTER
                textSize = 22f
                setTextColor(context.getColor(R.color.key_text))
                setOnClickListener { press(it); dismissPopup(); type(option) }
            }, LinearLayout.LayoutParams(anchor.width, anchor.height))
        }
        val origin = IntArray(2).also(this::getLocationInWindow)
        val pos = IntArray(2).also(anchor::getLocationInWindow)
        val params = LayoutParams(LayoutParams.WRAP_CONTENT, LayoutParams.WRAP_CONTENT).apply {
            leftMargin = (pos[0] - origin[0]).coerceAtMost(width - anchor.width * options.size).coerceAtLeast(0)
            topMargin = (pos[1] - origin[1] - anchor.height - dp(8)).coerceAtLeast(0)
        }
        addView(bar, params)
        popup = bar
    }

    private fun dismissPopup() {
        popup?.let(this::removeView)
        popup = null
    }

    private fun press(view: View) {
        view.performHapticFeedback(HapticFeedbackConstants.KEYBOARD_TAP)
        if (view.parent != popup) dismissPopup()
    }

    private fun dp(value: Int) = (value * resources.displayMetrics.density).toInt()
}
