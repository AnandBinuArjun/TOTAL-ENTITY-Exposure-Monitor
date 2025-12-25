package com.cortex.monitor

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import android.widget.TextView
import android.widget.Button
import android.view.View

class MainActivity : AppCompatActivity() {

    private lateinit var riskScoreView: TextView
    private lateinit var actionRecyclerView: RecyclerView
    private lateinit var scanButton: Button

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        riskScoreView = findViewById(R.id.riskScore)
        actionRecyclerView = findViewById(R.id.actionList)
        scanButton = findViewById(R.id.btnScan)

        setupUI()
    }

    private fun setupUI() {
        // In a real app, this would use Retrofit to call the FastAPI backend
        scanButton.setOnClickListener {
            performScan()
        }
    }

    private fun performScan() {
        riskScoreView.text = "72"
        riskScoreView.setTextColor(getColor(R.color.risk_high))
        
        // Mock Data Adapter would go here
    }
}
