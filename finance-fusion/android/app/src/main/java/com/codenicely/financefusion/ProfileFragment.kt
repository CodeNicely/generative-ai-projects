package com.codenicely.financefusion

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.fragment.app.Fragment


class ProfileFragment : Fragment() {

    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        // Inflate the layout for this fragment
        return inflater.inflate(R.layout.fragment_profile, container, false)
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        // Initialize views and set click listeners
        val imageViewProfilePicture = view.findViewById<ImageView>(R.id.imageViewProfilePicture)
        val textViewName = view.findViewById<TextView>(R.id.textViewName)
        val textViewEmail = view.findViewById<TextView>(R.id.textViewEmail)
        val buttonEditProfile = view.findViewById<Button>(R.id.buttonEditProfile)

        // Set click listener for edit profile button
        buttonEditProfile.setOnClickListener {
            // Navigate to edit profile screen
        }
    }

}