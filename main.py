from wallapop import get_all_product_ids, update_product


def main():
    product_ids = get_all_product_ids()
    for id in product_ids:
        status_code = update_product(id)
        print(f'id: {id}\tcode:{status_code}')


if __name__ == '__main__':
    main()
