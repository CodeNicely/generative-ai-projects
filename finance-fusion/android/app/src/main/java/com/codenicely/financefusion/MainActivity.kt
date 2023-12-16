package com.codenicely.financefusion

import android.os.Bundle
import android.widget.ImageView
import androidx.appcompat.app.AppCompatActivity
import androidx.core.view.GravityCompat
import androidx.drawerlayout.widget.DrawerLayout
import androidx.fragment.app.Fragment
import androidx.fragment.app.FragmentManager
import androidx.fragment.app.FragmentTransaction
import com.codenicely.financefusion.ui.ExpenseListFragment
import com.codenicely.financefusion.R
import com.google.android.material.navigation.NavigationView


class MainActivity : AppCompatActivity() {

    private lateinit var drawerLayout: DrawerLayout
    private lateinit var navigationView: NavigationView
    private lateinit var imageViewLogo: ImageView

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        drawerLayout = findViewById(R.id.drawerLayout)
        navigationView = findViewById(R.id.navigationView)
        imageViewLogo = findViewById(R.id.imageViewLogo)

        // Set up toolbar
        setSupportActionBar(findViewById(R.id.toolbar))
        supportActionBar?.setDisplayHomeAsUpEnabled(true)
        supportActionBar?.setHomeAsUpIndicator(R.drawable.baseline_menu_24)

        // Set up navigation drawer
        navigationView.setNavigationItemSelectedListener { menuItem ->
            when (menuItem.itemId) {
                R.id.menuItemAuthentication -> openFragment(AuthenticationFragment())
                R.id.menuItemProfile -> openFragment(ProfileFragment())
                R.id.menuItemExpenseList -> openFragment(ExpenseListFragment())
                R.id.menuItemAddExpense -> openFragment(AddExpenseFragment())
            }
            drawerLayout.closeDrawer(GravityCompat.START)
            true
        }

        imageViewLogo.setOnClickListener {
            drawerLayout.openDrawer(GravityCompat.START)
        }

        // Set default fragment
        openFragment(AuthenticationFragment())
    }

    private fun openFragment(fragment: Fragment) {
        val fragmentManager: FragmentManager = supportFragmentManager
        val fragmentTransaction: FragmentTransaction = fragmentManager.beginTransaction()
        fragmentTransaction.replace(R.id.frameLayoutContainer, fragment)
        fragmentTransaction.commit()
    }

    override fun onSupportNavigateUp(): Boolean {
        drawerLayout.openDrawer(GravityCompat.START)
        return true
    }

}