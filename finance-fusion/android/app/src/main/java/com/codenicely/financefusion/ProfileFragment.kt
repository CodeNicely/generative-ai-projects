package com.codenicely.financefusion

import android.os.Bundle
import androidx.fragment.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import com.codenicely.financefusion.R
import com.google.android.material.snackbar.Snackbar
import kotlinx.android.synthetic.main.fragment_profile.*

class ProfileFragment : Fragment() {

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        return inflater.inflate(R.layout.fragment_profile, container, false)
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        updateButton.setOnClickListener {
            val username = usernameTextInputLayout.editText?.text.toString()
            val email = emailTextInputLayout.editText?.text.toString()

            if (username.isEmpty() || email.isEmpty()) {
                Snackbar.make(view, "Please fill all fields", Snackbar.LENGTH_SHORT).show()
            } else {
                // TODO: Implement profile update functionality
            }
        }
    }
}