package com.codenicely.financefusion.ui

import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.recyclerview.widget.RecyclerView
import com.codenicely.financefusion.R

class ExpenseListAdapter : RecyclerView.Adapter<ExpenseListAdapter.ExpenseViewHolder>() {

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ExpenseViewHolder {
        val view = LayoutInflater.from(parent.context).inflate(R.layout.item_expense, parent, false)
        return ExpenseViewHolder(view)
    }

    override fun onBindViewHolder(holder: ExpenseViewHolder, position: Int) {
        // Bind data to views in the ViewHolder
    }

    override fun getItemCount(): Int {
        // Return the number of items in the list
        return 0
    }

    inner class ExpenseViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {
        // Declare views in the ViewHolder
    }

}