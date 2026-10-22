package uz.yangi.keyboard

import android.inputmethodservice.InputMethodService
import android.view.KeyEvent
import android.view.View
import android.view.inputmethod.EditorInfo
import android.view.inputmethod.InputMethodManager

class UzKeyboardService : InputMethodService(), KeyListener {

    private lateinit var layout: MobileLayout
    private var keyboard: KeyboardView? = null

    override fun onCreate() {
        super.onCreate()
        layout = MobileLayout.load(this)
    }

    override fun onCreateInputView(): View = KeyboardView(this, layout, this).also { keyboard = it }

    override fun onStartInputView(info: EditorInfo, restarting: Boolean) {
        super.onStartInputView(info, restarting)
        if (!restarting) keyboard?.reset()
        updateShift()
    }

    override fun onUpdateSelection(
        oldSelStart: Int, oldSelEnd: Int, newSelStart: Int, newSelEnd: Int,
        candidatesStart: Int, candidatesEnd: Int,
    ) {
        super.onUpdateSelection(oldSelStart, oldSelEnd, newSelStart, newSelEnd, candidatesStart, candidatesEnd)
        updateShift()
    }

    private fun updateShift() {
        val ic = currentInputConnection ?: return
        keyboard?.setAutoShift(ic.getCursorCapsMode(currentInputEditorInfo.inputType) != 0)
    }

    override fun onText(text: String) {
        currentInputConnection?.commitText(text, 1)
    }

    override fun onDelete() {
        sendDownUpKeyEvents(KeyEvent.KEYCODE_DEL)
    }

    override fun onEnter() {
        val options = currentInputEditorInfo.imeOptions
        val action = options and EditorInfo.IME_MASK_ACTION
        val noAction = (options and EditorInfo.IME_FLAG_NO_ENTER_ACTION) != 0 ||
            action == EditorInfo.IME_ACTION_NONE || action == EditorInfo.IME_ACTION_UNSPECIFIED
        if (noAction) sendDownUpKeyEvents(KeyEvent.KEYCODE_ENTER)
        else currentInputConnection?.performEditorAction(action)
    }

    override fun onGlobe(showPicker: Boolean) {
        if (showPicker || !switchToNextInputMethod(false)) {
            getSystemService(InputMethodManager::class.java).showInputMethodPicker()
        }
    }
}
