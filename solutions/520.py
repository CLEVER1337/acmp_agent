
def main():
    with open("INPUT.TXT", "r") as f:
        n = int(f.read().strip())
    
    # Цены
    price_pair = 10.5
    price_bundle = 102.5
    price_box = 1140
    
    # Единицы в упаковках
    pairs_in_bundle = 12
    bundles_in_box = 12
    pairs_in_box = pairs_in_bundle * bundles_in_box
    
    # Цены за пару в разных упаковках
    price_per_pair_in_pair = price_pair
    price_per_pair_in_bundle = price_bundle / pairs_in_bundle
    price_per_pair_in_box = price_box / pairs_in_box
    
    # Оптимальная стратегия: покупать максимально возможное количество
    # самых выгодных упаковок (коробок, затем связок, затем отдельных пар)
    
    boxes = n // pairs_in_box
    remaining = n % pairs_in_box
    
    bundles = remaining // pairs_in_bundle
    pairs = remaining % pairs_in_bundle
    
    # Проверяем, не выгоднее ли купить дополнительную связку вместо отдельных пар
    if pairs > 0:
        # Стоимость отдельных пар
        cost_pairs = pairs * price_per_pair_in_pair
        # Стоимость дополнительной связки
        cost_extra_bundle = price_bundle
        
        # Если связка дешевле отдельных пар
        if cost_extra_bundle <= cost_pairs:
            bundles += 1
            pairs = 0
    
    # Проверяем, не выгоднее ли купить дополнительную коробку вместо связок
    if bundles > 0:
        # Стоимость связок
        cost_bundles = bundles * price_bundle
        # Стоимость дополнительной коробки
        cost_extra_box = price_box
        
        # Если коробка дешевле связок
        if cost_extra_box <= cost_bundles:
            boxes += 1
            bundles = 0
    
    with open("OUTPUT.TXT", "w") as f:
        f.write(f"{boxes} {bundles} {pairs}")

if __name__ == "__main__":
    main()
