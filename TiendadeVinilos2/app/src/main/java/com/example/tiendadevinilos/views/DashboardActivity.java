package com.example.tiendadevinilos.views;

import android.content.Intent;
import android.os.Bundle;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;
import androidx.databinding.DataBindingUtil;
import androidx.lifecycle.ViewModelProvider;
import androidx.recyclerview.widget.LinearLayoutManager;

import com.example.tiendadevinilos.R;
import com.example.tiendadevinilos.adapters.ProductAdapter;
import com.example.tiendadevinilos.databinding.ActivityDashboardBinding;
import com.example.tiendadevinilos.viewmodels.DashboardViewModel;

import java.util.ArrayList;

public class DashboardActivity extends AppCompatActivity {

    private ProductAdapter productAdapter;
    private DashboardViewModel dashboardViewModel;
    private ActivityDashboardBinding binding;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        // Enlazar el layout con DataBinding
        binding = DataBindingUtil.setContentView(this, R.layout.activity_dashboard);

        // Configurar ViewModel y RecyclerView
        dashboardViewModel = new ViewModelProvider(this).get(DashboardViewModel.class);
        productAdapter = new ProductAdapter(new ArrayList<>(), product -> {
            Intent intent = new Intent(this, DetailActivity.class);
            intent.putExtra("id", product.getId());
            intent.putExtra("title", product.getTitle());
            intent.putExtra("description", product.getDescription());
            intent.putExtra("imageUrl", product.getImageUrl());
            startActivity(intent);
        });
        // Observador del ViewModel
        dashboardViewModel.getProductsLiveData().observe(this, products -> {
            if (products != null) {
                productAdapter.setProductList(products);
            } else {
                Toast.makeText(this, "Error al cargar los productos.", Toast.LENGTH_SHORT).show();
            }
        });
        binding.recyclerView.setLayoutManager(new LinearLayoutManager(this));
        binding.recyclerView.setAdapter(productAdapter);
        dashboardViewModel = new ViewModelProvider(this).get(DashboardViewModel.class);
        dashboardViewModel.getProductsLiveData().observe(this, products -> productAdapter.setProductList(products));


        // Configurar el botón de logout con binding
        binding.logoutButton.setOnClickListener(v -> {
            Intent intent = new Intent(DashboardActivity.this, LoginActivity.class);
            startActivity(intent);
            finish();
        });
    }
}
