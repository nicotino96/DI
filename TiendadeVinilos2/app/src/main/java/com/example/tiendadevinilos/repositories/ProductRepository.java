package com.example.tiendadevinilos.repositories;

import androidx.lifecycle.MutableLiveData;

import com.example.tiendadevinilos.models.Product;
import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;

import java.util.ArrayList;
import java.util.List;

public class ProductRepository {
    private final DatabaseReference productRef;

    public ProductRepository() {
        productRef = FirebaseDatabase.getInstance().getReference("items");
    }
    public void getProducts(MutableLiveData<List<Product>> productLiveData) {
        productRef.addValueEventListener(new ValueEventListener() {
            @Override
            public void onDataChange(DataSnapshot snapshot) {
                List<Product> products = new ArrayList<>();
                for (DataSnapshot child : snapshot.getChildren()) {
                    Product product = child.getValue(Product.class);
                    product.setId(child.getKey());
                    products.add(product);
                }
                productLiveData.setValue(products);
            }

            @Override
            public void onCancelled(DatabaseError error) {

            }
        });
    }
}
