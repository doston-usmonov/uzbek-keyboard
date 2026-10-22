package uz.yangi.keyboard

import android.content.Context
import org.json.JSONArray
import org.json.JSONObject

/** build.py yaratadigan assets/layout.json tartibi. */
class MobileLayout(
    val layers: Map<String, List<List<String>>>,
    val longPress: Map<String, List<String>>,
) {
    companion object {
        fun load(context: Context): MobileLayout {
            val json = JSONObject(context.assets.open("layout.json").bufferedReader().use { it.readText() })
            val layers = json.getJSONObject("layers")
            val longPress = json.getJSONObject("longpress")
            return MobileLayout(
                layers.keys().asSequence().associateWith { name ->
                    val rows = layers.getJSONArray(name)
                    List(rows.length()) { rows.getJSONArray(it).strings() }
                },
                longPress.keys().asSequence().associateWith { longPress.getJSONArray(it).strings() },
            )
        }

        private fun JSONArray.strings() = List(length()) { getString(it) }
    }
}
