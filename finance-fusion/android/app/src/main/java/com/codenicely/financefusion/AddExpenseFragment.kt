package com.codenicely.financefusion

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.fragment.app.Fragment


class AddExpenseFragment : Fragment() {

    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        // Inflate the layout for this fragment
        return inflater.inflate(R.layout.fragment_add_expense, container, false)
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        // Initialize views and set click listeners
        val textViewDate = view.findViewById<TextView>(R.id.textViewDate)
        val editTextAmount = view.findViewById<EditText>(R.id.editTextAmount)
        val spinnerCategory = view.findViewById<Spinner>(R.id.spinnerCategory)
        val editTextDescription = view.findViewById<EditText>(R.id.editTextDescription)
        val spinnerPaymentMethod = view.findViewById<Spinner>(R.id.spinnerPaymentMethod)
        val buttonAddExpense = view.findViewById<Button>(R.id.buttonAddExpense)

        // Set click listener for add expense button
        buttonAddExpense.setOnClickListener {
            // Perform add expense action
        }
    }

}