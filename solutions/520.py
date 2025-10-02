
def main():
    with open('INPUT.TXT', 'r') as f:
        n = int(f.read().strip())
    
    # Цены в копейках
    price_pair = 1050  # 10 руб 50 коп
    price_bundle = 10250  # 102 руб 50 коп
    price_box = 114000  # 1140 руб
    
    # Количество пар в связке и коробке
    pairs_in_bundle = 12
    pairs_in_box = 12 * pairs_in_bundle
    
    # Находим оптимальное количество коробок
    boxes = n // pairs_in_box
    remaining = n % pairs_in_box
    
    # Для оставшихся пар находим оптимальное количество связок
    bundles = remaining // pairs_in_bundle
    pairs = remaining % pairs_in_bundle
    
    # Проверяем, не выгоднее ли купить на одну связку больше
    if pairs > 0:
        # Стоимость покупки связками и отдельными парами
        cost_bundles_pairs = bundles * price_bundle + pairs * price_pair
        
        # Стоимость покупки на одну связку больше
        cost_extra_bundle = (bundles + 1) * price_bundle
        
        if cost_extra_bundle < cost_bundles_pairs:
            bundles += 1
            pairs = 0
    
    # Проверяем, не выгоднее ли купить на одну коробку больше
    if bundles == 12:
        boxes += 1
        bundles = 0
        pairs = 0
    elif bundles > 0 or pairs > 0:
        # Стоимость покупки коробками, связками и парами
        cost_current = boxes * price_box + bundles * price_bundle + pairs * price_pair
        
        # Стоимость покупки на одну коробку больше
        cost_extra_box = (boxes + 1) * price_box
        
        if cost_extra_box < cost_current:
            boxes += 1
            bundles = 0
            pairs = 0
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(f"{boxes} {bundles} {pairs}")

if __name__ == "__main__":
    main()
