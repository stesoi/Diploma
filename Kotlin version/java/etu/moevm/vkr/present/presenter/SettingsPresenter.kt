package etu.moevm.vkr.present.presenter

import android.content.Context
import android.net.ConnectivityManager
import com.arellomobile.mvp.InjectViewState
import com.arellomobile.mvp.MvpPresenter
import etu.moevm.vkr.present.view.SettingsView


@InjectViewState
class SettingsPresenter : MvpPresenter<SettingsView>() {
    fun hasConnection(context: Context?): Boolean {
        val cm =
            context?.getSystemService(Context.CONNECTIVITY_SERVICE) as ConnectivityManager
        var wifiInfo = cm.getNetworkInfo(ConnectivityManager.TYPE_WIFI)
        if (wifiInfo != null && wifiInfo.isConnected) {
            return true
        }
        wifiInfo = cm.getNetworkInfo(ConnectivityManager.TYPE_MOBILE)
        if (wifiInfo != null && wifiInfo.isConnected) {
            return true
        }
        wifiInfo = cm.activeNetworkInfo
        return if (wifiInfo != null && wifiInfo.isConnected) {
            true
        } else false
    }
}