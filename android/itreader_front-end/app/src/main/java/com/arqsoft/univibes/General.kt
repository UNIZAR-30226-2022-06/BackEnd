package com.arqsoft.univibes

import android.os.Bundle
import android.os.PersistableBundle
import androidx.appcompat.app.AppCompatActivity
import androidx.fragment.app.Fragment
import kotlinx.android.synthetic.main.general_activity.*

class General : AppCompatActivity(){
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.general_activity)

        val homeFragment = HomeFragment()
        val searchFragment = SearchFragment()
        val addEventFragment = AddEventFragment()
        val friendsFragment = FriendsFragment()
        val profileFragment = ProfileFragment()


        bottomNavigationView.setOnNavigationItemSelectedListener{
            when(it.itemId){
                R.id.nav_home -> {
                    setCurrentFragment(homeFragment)
                    true
                }
                R.id.nav_search -> {
                    setCurrentFragment(searchFragment)
                    true
                }
                R.id.nav_addEvent -> {
                    setCurrentFragment(addEventFragment)
                    true
                }
                R.id.nav_friends -> {
                    setCurrentFragment(friendsFragment)
                    true
                }
                R.id.nav_profile -> {
                    setCurrentFragment(profileFragment)
                    true
                }
                else -> false
            }
        }
    }

    private fun setCurrentFragment(fragment: Fragment){
        supportFragmentManager.beginTransaction().apply {
            replace(R.id.containerView, fragment)
            commit()
        }
    }


}