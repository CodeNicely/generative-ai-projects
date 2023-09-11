package com.codenicely.financefusion.ui

import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import androidx.recyclerview.widget.RecyclerView

class ExpenseListAdapter(private val expenseList: List<Expense>) : RecyclerView.Adapter<ExpenseListAdapter.ExpenseViewHolder>() {

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ExpenseViewHolder {
        val view = LayoutInflater.from(parent.context).inflate(R.layout.item_expense, parent, false)
        return ExpenseViewHolder(view)
    }

    override fun onBindViewHolder(holder: ExpenseViewHolder, position: Int) {
        val expense = expenseList[position]
        holder.bind(expense)
    }

    override fun getItemCount(): Int {
        return expenseList.size
    }

    inner class ExpenseViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {

        private val textViewExpenseTitle: TextView = itemView.findViewById(R.id.textViewExpenseTitle)
        private val textViewExpenseAmount: TextView = itemView.findViewById(R.id.textViewExpenseAmount)
        private val textViewExpenseCategory: TextView = itemView.findViewById(R.id.textViewExpenseCategory)

        fun bind(expense: Expense) {
            textViewExpenseTitle.text = expense.title
            textViewExpenseAmount.text = expense.amount.toString()
            textViewExpenseCategory.text = expense.category
        }

    }

}
