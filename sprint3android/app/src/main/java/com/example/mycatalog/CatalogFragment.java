package com.example.mycatalog;

import android.content.Intent;
import android.os.Bundle;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;

public class CatalogFragment extends Fragment {

    /**
     * Método para inflar y configurar el layout del fragmento.
     *
     * @param inflater           Objeto utilizado para inflar vistas en el fragmento.
     * @param container          Contenedor padre al que se añadirá la vista del fragmento (puede ser nulo).
     * @param savedInstanceState Estado guardado previamente (si existe).
     * @return La vista inflada del fragmento.
     */
    @Nullable
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.fragment_catalog, container, false);
        Button button = view.findViewById(R.id.button_catalog_fragment);
        button.setOnClickListener(v -> {
            Intent intent = new Intent(requireContext(), DetailActivity.class);
            startActivity(intent);
            requireActivity().finish();
        });
        return view;
    }
}