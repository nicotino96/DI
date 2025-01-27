package com.example.tiendadevinilos.models;

public class Product {
    private String id;
    private String name;
    private String description;

    public Product() {}

    public Product(String id, String name, String price) {
        this.id = id;
        this.name = name;
        this.description = price;
    }

    public String getId() { return id; }
    public String getName() { return name; }
    public String getDescription() { return description; }
}
