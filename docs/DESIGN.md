# Design Document

## Data Models

The design of the `Map My World` API revolves around three key data models: **Locations**, **Categories**, and **Location-Category Reviews**. These models ensure that the application can handle location data, categorize it effectively, and maintain review integrity.

### Locations (`locations`)

**Purpose**: Represents specific places on the map with geographic and descriptive details.

**Fields**:

- `id` (int): Unique identifier for the location.
- `latitude` (float): Latitude coordinate of the location.
- `longitude` (float): Longitude coordinate of the location.
- `name` (string): Name of the location.
- `formatted_address` (string, optional): Full address of the location.
- `formatted_phone_number` (string, optional): Contact number for the location.
- `rating` (float, optional): Average rating for the location.
- `website` (string, optional): Website URL for the location.
- `serves_brunch` (boolean): Indicates if the location serves brunch.
- `serves_dinner` (boolean): Indicates if the location serves dinner.
- `serves_lunch` (boolean): Indicates if the location serves lunch.

### Categories (`categories`)

**Purpose**: Represents various types of locations.

**Fields**:

- `id` (int): Unique identifier for the category.
- `name` (string): Name of the category (e.g., "Restaurant", "Park").

### Location-Category Reviews (`location_category_reviewed`)

**Purpose**: Tracks the review status of location-category combinations to ensure recommendations remain relevant.

**Fields**:

- `location_id` (int): Foreign key referencing a location.
- `category_id` (int): Foreign key referencing a category.
- `last_reviewed` (datetime): The last time this combination was reviewed.

## Relationships Between Models

- **One-to-Many**:
  - A single category can be associated with multiple locations.
- **Many-to-Many**:
  - The `Location-Category Reviews` table serves as a bridge table between `locations` and `categories`.

## Validation Rules

1. **Latitude**: Must be between -90 and 90.
2. **Longitude**: Must be between -180 and 180.
3. **Unique Constraints**:
   - Each `location_id` and `category_id` pair in the `Location-Category Reviews` table must be unique.
