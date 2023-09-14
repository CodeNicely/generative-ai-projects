package com.codenicely.financefusion.ui

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.fragment.app.Fragment


class ExpenseListFragment : Fragment() {

    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        // Inflate the layout for this fragment
        return inflater.inflate(R.layout.fragment_expense_list, container, false)
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        // Initialize views and set up RecyclerView
        val recyclerViewExpenseList = view.findViewById<RecyclerView>(R.id.recyclerViewExpenseList)
        recyclerViewExpenseList.layoutManager = LinearLayoutManager(requireContext())

        // Set up adapter for RecyclerView
        val expenseListAdapter = ExpenseListAdapter()
        recyclerViewExpenseList.adapter = expenseListAdapter
    }

}