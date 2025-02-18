package com.example.tiendadevinilos.views;

import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Toast;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;
import androidx.lifecycle.ViewModelProvider;
import androidx.recyclerview.widget.LinearLayoutManager;

import com.example.tiendadevinilos.adapters.ProductAdapter;
import com.example.tiendadevinilos.databinding.FragmentFavouritesBinding;
import com.example.tiendadevinilos.viewmodels.FavouritesViewModel;

import java.util.ArrayList;

public class FavouritesFragment extends Fragment {

    private FragmentFavouritesBinding binding;
    private FavouritesViewModel viewModel;
    private ProductAdapter adapter;

    @Nullable
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater,
                             @Nullable ViewGroup container,
                             @Nullable Bundle savedInstanceState) {
        binding = FragmentFavouritesBinding.inflate(inflater, container, false);
        return binding.getRoot();
    }

    @Override
    public void onViewCreated(@NonNull View view,
                              @Nullable Bundle savedInstanceState) {
        super.onViewCreated(view, savedInstanceState);
        Log.d("FavouritesFragment", "onViewCreated() called");

        // Instanciar el ViewModel
        viewModel = new ViewModelProvider(this).get(FavouritesViewModel.class);

        // Configurar RecyclerView con el adaptador
        adapter = new ProductAdapter(new ArrayList<>(), product -> {
            // Abrir DetailActivity al hacer clic en un favorito
            Intent intent = new Intent(requireContext(), DetailActivity.class);
            intent.putExtra("id", product.getId());
            intent.putExtra("title", product.getTitle());
            intent.putExtra("description", product.getDescription());
            intent.putExtra("imageUrl", product.getImageUrl());
            startActivity(intent);
        });
        binding.recyclerView.setLayoutManager(new LinearLayoutManager(requireContext()));
        binding.recyclerView.setAdapter(adapter);

        // Llamar a loadFavorites() para descargar la lista
        Log.d("FavouritesFragment", "Cargando favoritos...");
        viewModel.loadFavorites();

        // Observar los datos
        viewModel.getFavorites().observe(getViewLifecycleOwner(), favorites -> {
            if (favorites != null && !favorites.isEmpty()) {
                Log.d("FavouritesFragment", "Favoritos recibidos: " + favorites.size());
                adapter.setProductList(favorites);
            } else {
                Log.d("FavouritesFragment", "Lista de favoritos vacía");
                Toast.makeText(requireContext(), "No tienes favoritos", Toast.LENGTH_SHORT).show();
            }
        });
    }

    @Override
    public void onDestroyView() {
        super.onDestroyView();
        binding = null; // Evitar memory leaks
    }
}
