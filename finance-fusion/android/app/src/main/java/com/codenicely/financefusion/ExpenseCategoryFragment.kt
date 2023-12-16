package com.codenicely.financefusion

import android.os.Bundle
import androidx.fragment.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.recyclerview.widget.LinearLayoutManager
import com.codenicely.financefusion.R
import kotlinx.android.synthetic.main.fragment_expense_category.*

class ExpenseCategoryFragment : Fragment() {

//    private lateinit var adapter: ExpenseCategoryAdapter

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        return inflater.inflate(R.layout.fragment_expense_category, container, false)
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        recyclerView.layoutManager = LinearLayoutManager(context)
//        adapter = ExpenseCategoryAdapter()
//        recyclerView.adapter = adapter

        // TODO: Load expense categories
    }
}