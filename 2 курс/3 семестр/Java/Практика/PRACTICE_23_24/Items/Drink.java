package Items;

public final class Drink implements Item, Alcoholable {
	private final String name;
	private final String description;
	private final Integer price;
	private final Double alcoholVol;
	private final DrinkTypeENUM type;

	public Drink(String name, String description, DrinkTypeENUM type) {
		this.type = type;
		this.name = name;
		this.description = description;
		this.price = 0;
		this.alcoholVol = 0.0;
	}

	public Drink(String name, String description, Integer price, DrinkTypeENUM type) {
		this.type = type;
		this.name = name;
		this.description = description;
		this.price = price;
		this.alcoholVol = 0.0;
	}

	public Drink(String name, String description, Integer price, Double alcoholVol, DrinkTypeENUM type) {
		this.type = type;
		this.name = name;
		this.description = description;
		this.price = price;
		this.alcoholVol = alcoholVol;
	}

	@Override
	public String getName() {
		return name;
	}

	@Override
	public String getDescription() {
		return description;
	}

	@Override
	public Integer getPrice() {
		return price;
	}

	@Override
	public boolean isAlcoholicDrink() {
		return alcoholVol > 0.0;
	}

	@Override
	public double getAlcoholVol() {
		return alcoholVol;
	}

	public DrinkTypeENUM getType() {
		return type;
	}

	@Override
	public String toString() {
		return name + ": " + description + ". Цена: " + price + "$";
	}

	@Override
	public int compareTo(Item o) {
		return -(price.compareTo(o.getPrice()));
	}
}
