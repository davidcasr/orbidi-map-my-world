# Technical Challenge: "Map My World"

## Introduction to the Challenge

Imagine you are building the backend for **'Map My World'**, an application designed to explore and review various locations and categories around the world, such as restaurants, parks, and museums. The goal is to provide users with an interactive map where they can discover new locations and see recommendations based on specific categories. However, there is a twist: we want to ensure that recommendations are always up-to-date and relevant.

## Your Mission

As part of the development team for **'Map My World'**, your task is to build the core of our application: a **REST API** that manages the logic for adding new locations and categories. More importantly, you must implement a special feature that allows us to keep our recommendations fresh and engaging for our users.

## Technologies

This challenge must be implemented using **Python** and **FastAPI**.

## Technical Specifications

### **Data Models**

- **Locations (`locations`)**: Each location has a longitude and latitude.
- **Categories (`categories`)**: Each category represents a type of place to explore.
- **Location-Category Reviews (`location_category_reviewed`)**: This record ensures quality control, guaranteeing that each location-category combination is reviewed regularly.

### **Key Features**

- **Location and Category Management**: Allows API users to add new locations and categories.
- **Exploration Recommender**: A special endpoint that suggests 10 location-category combinations that have not been reviewed in the last 30 days, prioritizing those that have never been reviewed.

## Objectives

1. **Clarity and Structure**:

   - Your code must be clear and well-structured.
   - We want to see how you organize your project and apply coding best practices.

2. **Efficiency and Optimization**:

   - Recommendations must be generated efficiently, considering both response speed and resource usage.

3. **Documentation**:
   - A good API is not just about the code; it is also about how you communicate its usage to other developers.
   - We expect to see thorough documentation of endpoints and models.
