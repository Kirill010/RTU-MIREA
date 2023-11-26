package Customer;

public final class Address {

    private static final Address EMPTY_ADDRESS = new Address();

    private final String cityName;
    private final String streetName;
    private final int zipCode;
    private final int buildingNumber;
    private final int apartmentNumber;
    private final char buildingLetter;

    public Address(String address) {
        String[] parseAddress = address.split("\\,");

        this.cityName = parseAddress[0];
        this.streetName = parseAddress[1];
        this.zipCode = Integer.parseInt(parseAddress[2]);
        this.buildingNumber = Integer.parseInt(parseAddress[3]);
        this.apartmentNumber = Integer.parseInt(parseAddress[4]);
        this.buildingLetter = parseAddress[5].charAt(0);
    }

    public Address() {
        this.cityName = "cityName";
        this.streetName = "streetName";
        this.zipCode = 0;
        this.buildingNumber = 0;
        this.apartmentNumber = 0;
        this.buildingLetter = 'l';
    }

    public String getCityName() {
        return cityName;
    }

    public String getStreetName() {
        return streetName;
    }

    public int getZipCode() {
        return zipCode;
    }

    public int getBuildingNumber() {
        return buildingNumber;
    }

    public int getApartmentNumber() {
        return apartmentNumber;
    }

    public char getBuildingLetter() {
        return buildingLetter;
    }

    @Override
    public String toString() {
        return "Город: " + cityName +
                "\nУлица: " + streetName +
                "\nИндекс: " + zipCode +
                "\nДом: " + buildingNumber +
                "\nКвартира: " + apartmentNumber +
                "\nСтроение: " + buildingLetter;
    }
}
