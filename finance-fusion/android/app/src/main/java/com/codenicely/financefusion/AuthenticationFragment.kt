package com.codenicely.financefusion

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.fragment.app.Fragment


class AuthenticationFragment : Fragment() {

    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        // Inflate the layout for this fragment
        return inflater.inflate(R.layout.fragment_authentication, container, false)
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        // Initialize views and set click listeners
        val imageViewLogo = view.findViewById<ImageView>(R.id.imageViewLogo)
        val editTextEmail = view.findViewById<EditText>(R.id.editTextEmail)
        val editTextPassword = view.findViewById<EditText>(R.id.editTextPassword)
        val buttonLogin = view.findViewById<Button>(R.id.buttonLogin)
        val textViewRegister = view.findViewById<TextView>(R.id.textViewRegister)

        // Set click listener for login button
        buttonLogin.setOnClickListener {
            // Perform login action
        }

        // Set click listener for register text view
        textViewRegister.setOnClickListener {
            // Navigate to register screen
        }
    }

}