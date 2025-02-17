package com.example.tiendadevinilos.views;

import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.util.Log;
import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;
import androidx.appcompat.app.AppCompatDelegate;
import androidx.core.content.ContextCompat;
import androidx.lifecycle.ViewModelProvider;
import com.bumptech.glide.Glide;
import com.example.tiendadevinilos.R;
import com.example.tiendadevinilos.databinding.ActivityDetailBinding;
import com.example.tiendadevinilos.viewmodels.DetailViewModel;

public class DetailActivity extends AppCompatActivity {
    private ActivityDetailBinding binding;
    private DetailViewModel viewModel;

    private String productId;

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        // Recuperar SharedPreferences antes de inflar la vista


        super.onCreate(savedInstanceState);
        binding = ActivityDetailBinding.inflate(getLayoutInflater());
        setContentView(binding.getRoot());

        viewModel = new ViewModelProvider(this).get(DetailViewModel.class);

        // Obtener datos del Intent (producto seleccionado)
        productId = getIntent().getStringExtra("id");
        String title = getIntent().getStringExtra("title");
        String description = getIntent().getStringExtra("description");
        String imageUrl = getIntent().getStringExtra("imageUrl");

        if (productId == null) {
            Log.e("DetailActivity", "Error: productId es NULL");
            return;
        }

        // Asignar datos a la interfaz
        binding.productTitle.setText(title);
        binding.productDescription.setText(description);
        Glide.with(this).load(imageUrl).into(binding.productImage);

        // Configurar botón de favorito
        binding.fabFavorite.setOnClickListener(v -> {
            Log.d("DetailActivity", "Se hizo clic en el botón de favoritos");
            viewModel.toggleFavorite(productId);
        });

        // Verificar si el producto es favorito y observar cambios
        viewModel.checkIfFavorite(productId);
        viewModel.getIsFavorite().observe(this, isFav -> {
            Log.d("DetailActivity", "Estado de favorito cambiado a: " + isFav);
            binding.fabFavorite.setImageDrawable(
                    ContextCompat.getDrawable(this,
                            Boolean.TRUE.equals(isFav) ?
                                    R.drawable.ic_favorite :
                                    R.drawable.ic_favorite_border
                    )
            );
        });

        // Configurar el ToggleButton de modo oscuro con SharedPreferences

    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
        // Eliminar observadores para evitar fugas de memoria
        viewModel.getIsFavorite().removeObservers(this);
    }
}
