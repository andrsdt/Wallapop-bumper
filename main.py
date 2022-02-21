from wallapop import get_all_product_ids, update_product


def main():
    product_ids = get_all_product_ids()
    for id in product_ids:
        update_product(id)


if __name__ == '__main__':
    main()
