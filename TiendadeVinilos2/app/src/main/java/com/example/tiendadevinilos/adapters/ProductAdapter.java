package com.example.tiendadevinilos.adapters;

import android.view.LayoutInflater;
import android.view.ViewGroup;
import androidx.databinding.DataBindingUtil;
import androidx.recyclerview.widget.RecyclerView;
import androidx.annotation.NonNull;

import com.bumptech.glide.Glide;
import com.example.tiendadevinilos.R;
import com.example.tiendadevinilos.databinding.ItemProductBinding;
import com.example.tiendadevinilos.models.Product;

import java.util.List;

public class ProductAdapter extends RecyclerView.Adapter<ProductAdapter.ProductViewHolder> {
    private List<Product> productList;
    private static OnItemClickListener listener = null;
    public ProductAdapter(List<Product> products, OnItemClickListener listener) {
        this.productList = products;
        ProductAdapter.listener = listener;
    }

    public void setProductList(List<Product> productList) {
        this.productList = productList;
        notifyDataSetChanged();
    }

    @NonNull
    @Override
    public ProductViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        ItemProductBinding binding = DataBindingUtil.inflate(
                LayoutInflater.from(parent.getContext()),
                R.layout.item_product,
                parent,
                false);
        return new ProductViewHolder(binding);
    }

    @Override
    public void onBindViewHolder(@NonNull ProductViewHolder holder, int position) {
        Product product = productList.get(position);
        holder.bind(product);
    }

    @Override
    public int getItemCount() {
        return productList != null ? productList.size() : 0;
    }

    public interface OnItemClickListener {
        void onItemClick(Product product);
    }

    static class ProductViewHolder extends RecyclerView.ViewHolder {
        private final ItemProductBinding binding;
        public ProductViewHolder(@NonNull ItemProductBinding binding) {
            super(binding.getRoot());
            this.binding = binding;
        }
        public void bind(Product product) {
            binding.setProduct(product);
            binding.executePendingBindings();
            binding.getRoot().setOnClickListener(v ->
                    listener.onItemClick(product));
            Glide.with(binding.getRoot().getContext())
                    .load(product.getImageUrl())
                    .placeholder(R.drawable.placeholder) // Imagen mientras carga
                    .error(R.drawable.error) // Imagen si hay error
                    .into(binding.imageUrl); // Asegúrate de que el ID del ImageView coincide

            binding.getRoot().setOnClickListener(v -> listener.onItemClick(product));
        }

    }
}
