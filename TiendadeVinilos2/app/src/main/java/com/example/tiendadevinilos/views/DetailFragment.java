package com.example.tiendadevinilos.views;

import android.content.Context;
import android.os.Bundle;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.core.content.ContextCompat;
import androidx.fragment.app.Fragment;
import androidx.lifecycle.ViewModelProvider;
import com.bumptech.glide.Glide;
import com.example.tiendadevinilos.R;
import com.example.tiendadevinilos.databinding.FragmentDetailBinding;
import com.example.tiendadevinilos.viewmodels.DetailViewModel;

public class DetailFragment extends Fragment {
    private FragmentDetailBinding binding;
    private DetailViewModel viewModel;
    private String productId;

    @Nullable
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        binding = FragmentDetailBinding.inflate(inflater, container, false);
        return binding.getRoot();
    }

    @Override
    public void onViewCreated(@NonNull View view, @Nullable Bundle savedInstanceState) {
        super.onViewCreated(view, savedInstanceState);

        viewModel = new ViewModelProvider(this).get(DetailViewModel.class);

        // Obtener los datos pasados desde el fragmento anterior
        if (getArguments() != null) {
            productId = getArguments().getString("id");
            String title = getArguments().getString("title");
            String description = getArguments().getString("description");
            String imageUrl = getArguments().getString("imageUrl");

            // Asignar datos a la interfaz
            binding.productTitle.setText(title);
            binding.productDescription.setText(description);
            Glide.with(this).load(imageUrl).into(binding.productImage);
        } else {
            Log.e("DetailFragment", "Error: No se recibieron argumentos");
            return;
        }

        // Configurar botón de favorito
        binding.fabFavorite.setOnClickListener(v -> {
            Log.d("DetailFragment", "Se hizo clic en el botón de favoritos");
            viewModel.toggleFavorite(productId);
        });

        // Verificar si el producto es favorito y observar cambios
        viewModel.checkIfFavorite(productId);
        viewModel.getIsFavorite().observe(getViewLifecycleOwner(), isFav -> {
            Log.d("DetailFragment", "Estado de favorito cambiado a: " + isFav);
            binding.fabFavorite.setImageDrawable(
                    ContextCompat.getDrawable(requireContext(),
                            Boolean.TRUE.equals(isFav) ?
                                    R.drawable.ic_favorite :
                                    R.drawable.ic_favorite_border
                    )
            );
        });
    }

    @Override
    public void onDestroyView() {
        super.onDestroyView();
        viewModel.getIsFavorite().removeObservers(getViewLifecycleOwner());
        binding = null; // Evitar memory leaks
    }
}

