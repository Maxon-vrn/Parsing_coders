from numpy import product
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
ua = UserAgent()

print()
"""Данный парсер собирает данные о ноутбуках Huawei: модель,характеристики, цена"""
"""При частом повторном использовании сервер блокирует запросы"""

def pars_product():
    
    cookies = {
    'directCrm-session': '%7B%22deviceGuid%22%3A%22b811bb12-90bf-46d1-8058-f6e0a75b4c0f%22%7D',
    'mindboxDeviceUUID': 'b811bb12-90bf-46d1-8058-f6e0a75b4c0f',
    'MVID_ENVCLOUD': 'prod1',
    'CACHE_INDICATOR': 'false',
    'COMPARISON_INDICATOR': 'false',
    'JSESSIONID': 'nWBZvXHGHyBJfpXr4DkFQyy39VxKG3svmGcT8LSV4zzS2ZJDfj1f!671526684',
    'MVID_CITY_ID': 'CityCZ_7173',
    'MVID_KLADR_ID': '3600000100000',
    'MVID_REGION_ID': '14',
    'MVID_REGION_SHOP': 'S921',
    'MVID_TIMEZONE_OFFSET': '3',
    'bIPs': '-1707567431',
    'flacktory': 'no',
    'tmr_reqNum': '20',
    'tmr_detect': '0%7C1658308156084',
    'afUserId': '9316a75c-a586-4557-9ae1-185ef9fd2a02-p',
    '_ga': 'GA1.2.247245394.1658305903',
    '_gid': 'GA1.2.1452565127.1658305903',
    'tmr_lvid': '2f9d22d3ecc41d096f4b699dd1016766',
    'tmr_lvidTS': '1658305905935',
    '_ga_BNX5WPP3YK': 'GS1.1.1658308146.2.1.1658308150.56',
    '_ga_CFMZTSS5FM': 'GS1.1.1658308146.2.1.1658308150.0',
    'MVID_CITY_CHANGED': 'false',
    'MVID_GEOLOCATION_NEEDED': 'false',
    'cookie_ip_add': '45.150.27.91',
    '__ttl__widget__ui': '1658306052607-040f688ecf58',
    'gdeslon.ru.__arc_domain': 'gdeslon.ru',
    'gdeslon.ru.user_id': 'b791052a-e0bd-4a41-9a19-44bf0039c749',
    'AF_SYNC': '1658305906677',
    'flocktory-uuid': '91ca5287-9047-43f1-8ca8-214a4ed3dd5c-1',
    'st_uid': '344642d99d71d47587cf891bed36c1fd',
    'advcake_session_id': '0390c1f0-1e9f-994b-d6fa-9f60f3d3ed5c',
    'advcake_track_id': 'd94067f8-30f8-2031-4116-d759e20d321a',
    'uxs_uid': '63e76b10-0806-11ed-8663-db5d7805e95b',
    '_ym_d': '1658305904',
    '_ym_isad': '2',
    '_ym_uid': '1658305904213173740',
    'MVID_2_exp_in_1': '1',
    'MVID_CART_AVAILABILITY': '2',
    'MVID_CREDIT_AVAILABILITY': 'true',
    'MVID_GTM_DELAY': 'true',
    'MVID_LP_SOLD_VARIANTS': '3',
    'MVID_MCLICK': 'true',
    'MVID_MOBILE_FILTERS': 'false',
    'MVID_NEW_LK': 'true',
    'MVID_NEW_LK_LOGIN': 'true',
    'MVID_SMART_BANNER_BOTTOM': 'true',
    'MVID_SUPER_FILTERS': 'true',
    '__lhash_': '8821f852021d0104116066f8c9dcac16',
    'MAIN_PAGE_VARIATION': '5',
    'MVID_ABC_TEST_WIDGET': '0',
    'MVID_AB_PROMO_DAILY': '1',
    'MVID_AB_SERVICES_DESCRIPTION': 'var2',
    'MVID_AB_TEST_COMPARE_ONBOARDING': 'true',
    'MVID_BLACK_FRIDAY_ENABLED': 'true',
    'MVID_CATALOG_STATE': '1',
    'MVID_FILTER_CODES': 'true',
    'MVID_FILTER_TOOLTIP': '1',
    'MVID_FLOCKTORY_ON': 'true',
    'MVID_GIFT_KIT': 'true',
    'MVID_IS_NEW_BR_WIDGET': 'true',
    'MVID_LAYOUT_TYPE': '1',
    'MVID_NEW_ACCESSORY': 'true',
    'MVID_NEW_DESKTOP_FILTERS': 'true',
    'MVID_NEW_LK_CHECK_CAPTCHA': 'true',
    'MVID_NEW_LK_OTP_TIMER': 'true',
    'MVID_NEW_MBONUS_BLOCK': 'true',
    'MVID_PRICE_FIRST': '2',
    'MVID_PRM20_CMS': 'true',
    'MVID_SERVICES': '111',
    'MVID_SERVICES_MINI_BLOCK': 'var2',
    'MVID_WEBP_ENABLED': 'true',
    'HINTS_FIO_COOKIE_NAME': '1',
    'MVID_ADDRESS_COMMENT_AB_TEST': '2',
    'MVID_CALC_BONUS_RUBLES_PROFIT': 'true',
    'MVID_CART_MULTI_DELETE': 'true',
    'MVID_CHECKOUT_REGISTRATION_AB_TEST': '2',
    'MVID_GET_LOCATION_BY_DADATA': 'DaData',
    'MVID_GUEST_ID': '20612185933',
    'MVID_TAXI_DELIVERY_INTERVALS_VIEW': 'new',
    'NEED_REQUIRE_APPLY_DISCOUNT': 'true',
    'PRESELECT_COURIER_DELIVERY_FOR_KBT': 'false',
    'PROMOLISTING_WITHOUT_STOCK_AB_TEST': '2',
    'searchType2': '3',
}

    headers = {
    # Already added when you pass json=
    # 'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Accept-Language': 'ru',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Host': 'www.mvideo.ru',
    'Origin': 'https://www.mvideo.ru',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Safari/605.1.15',
    'Connection': 'keep-alive',
    'Referer': 'https://www.mvideo.ru/noutbuki-planshety-komputery-8/noutbuki-118/f/brand=huawei/tolko-v-nalichii=da/kolichestvo-yader=4,6/razreshenie-ekrana=2160x1440-piks,2560x1440-piks,2880x1800-piks,3000x2000-piks,3300x2200-piks,3840x2160-piks,3840x2400-piks?sort=price_asc',
    # 'Content-Length': '261',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'directCrm-session=%7B%22deviceGuid%22%3A%22b811bb12-90bf-46d1-8058-f6e0a75b4c0f%22%7D; mindboxDeviceUUID=b811bb12-90bf-46d1-8058-f6e0a75b4c0f; MVID_ENVCLOUD=prod1; CACHE_INDICATOR=false; COMPARISON_INDICATOR=false; JSESSIONID=nWBZvXHGHyBJfpXr4DkFQyy39VxKG3svmGcT8LSV4zzS2ZJDfj1f!671526684; MVID_CITY_ID=CityCZ_7173; MVID_KLADR_ID=3600000100000; MVID_REGION_ID=14; MVID_REGION_SHOP=S921; MVID_TIMEZONE_OFFSET=3; bIPs=-1707567431; flacktory=no; tmr_reqNum=20; tmr_detect=0%7C1658308156084; afUserId=9316a75c-a586-4557-9ae1-185ef9fd2a02-p; _ga=GA1.2.247245394.1658305903; _gid=GA1.2.1452565127.1658305903; tmr_lvid=2f9d22d3ecc41d096f4b699dd1016766; tmr_lvidTS=1658305905935; _ga_BNX5WPP3YK=GS1.1.1658308146.2.1.1658308150.56; _ga_CFMZTSS5FM=GS1.1.1658308146.2.1.1658308150.0; MVID_CITY_CHANGED=false; MVID_GEOLOCATION_NEEDED=false; cookie_ip_add=45.150.27.91; __ttl__widget__ui=1658306052607-040f688ecf58; gdeslon.ru.__arc_domain=gdeslon.ru; gdeslon.ru.user_id=b791052a-e0bd-4a41-9a19-44bf0039c749; AF_SYNC=1658305906677; flocktory-uuid=91ca5287-9047-43f1-8ca8-214a4ed3dd5c-1; st_uid=344642d99d71d47587cf891bed36c1fd; advcake_session_id=0390c1f0-1e9f-994b-d6fa-9f60f3d3ed5c; advcake_track_id=d94067f8-30f8-2031-4116-d759e20d321a; uxs_uid=63e76b10-0806-11ed-8663-db5d7805e95b; _ym_d=1658305904; _ym_isad=2; _ym_uid=1658305904213173740; MVID_2_exp_in_1=1; MVID_CART_AVAILABILITY=2; MVID_CREDIT_AVAILABILITY=true; MVID_GTM_DELAY=true; MVID_LP_SOLD_VARIANTS=3; MVID_MCLICK=true; MVID_MOBILE_FILTERS=false; MVID_NEW_LK=true; MVID_NEW_LK_LOGIN=true; MVID_SMART_BANNER_BOTTOM=true; MVID_SUPER_FILTERS=true; __lhash_=8821f852021d0104116066f8c9dcac16; MAIN_PAGE_VARIATION=5; MVID_ABC_TEST_WIDGET=0; MVID_AB_PROMO_DAILY=1; MVID_AB_SERVICES_DESCRIPTION=var2; MVID_AB_TEST_COMPARE_ONBOARDING=true; MVID_BLACK_FRIDAY_ENABLED=true; MVID_CATALOG_STATE=1; MVID_FILTER_CODES=true; MVID_FILTER_TOOLTIP=1; MVID_FLOCKTORY_ON=true; MVID_GIFT_KIT=true; MVID_IS_NEW_BR_WIDGET=true; MVID_LAYOUT_TYPE=1; MVID_NEW_ACCESSORY=true; MVID_NEW_DESKTOP_FILTERS=true; MVID_NEW_LK_CHECK_CAPTCHA=true; MVID_NEW_LK_OTP_TIMER=true; MVID_NEW_MBONUS_BLOCK=true; MVID_PRICE_FIRST=2; MVID_PRM20_CMS=true; MVID_SERVICES=111; MVID_SERVICES_MINI_BLOCK=var2; MVID_WEBP_ENABLED=true; HINTS_FIO_COOKIE_NAME=1; MVID_ADDRESS_COMMENT_AB_TEST=2; MVID_CALC_BONUS_RUBLES_PROFIT=true; MVID_CART_MULTI_DELETE=true; MVID_CHECKOUT_REGISTRATION_AB_TEST=2; MVID_GET_LOCATION_BY_DADATA=DaData; MVID_GUEST_ID=20612185933; MVID_TAXI_DELIVERY_INTERVALS_VIEW=new; NEED_REQUIRE_APPLY_DISCOUNT=true; PRESELECT_COURIER_DELIVERY_FOR_KBT=false; PROMOLISTING_WITHOUT_STOCK_AB_TEST=2; searchType2=3',
    'x-set-application-id': 'b6636c03-14c5-46f6-a816-d0647b74203d',
}

    json_data = {
    'productIds': [
        '30062804',
        '30059533',
        '30062803',
        '30059532',
        '30059531',
        '30059530',
        '30058014',
        '30058015',
    ],
    'mediaTypes': [
        'images',
    ],
    'category': True,
    'status': True,
    'brand': True,
    'propertyTypes': [
        'KEY',
    ],
    'propertiesConfig': {
        'propertiesPortionSize': 5,
    },
    'multioffer': False,
}

    response = requests.post('https://www.mvideo.ru/bff/product-details/list', cookies=cookies, headers=headers, json=json_data).json()
    product_id = response.get('body').get('products')

    dict_copm = {}
    for i in product_id:
        value = []
        #print(i['name'])
        #print('id = ',i['materialCisNumber'])
        #print(i['propertiesPortion'][0]['name'],i['propertiesPortion'][0]['value'])
        #print(i['propertiesPortion'][1]['name'],i['propertiesPortion'][1]['value'])
        #print(i['propertiesPortion'][2]['name'],i['propertiesPortion'][2]['value'])
        #print(i['propertiesPortion'][3]['name'],i['propertiesPortion'][3]['value'])
        #print(i['propertiesPortion'][4]['name'],i['propertiesPortion'][4]['value'])
        value.append(i['name'])
        value.append(i['propertiesPortion'][0]['name'])
        value.append(i['propertiesPortion'][0]['value'])
        value.append(i['propertiesPortion'][1]['name'])      
        value.append(i['propertiesPortion'][1]['value'])
        value.append(i['propertiesPortion'][2]['name'])
        value.append(i['propertiesPortion'][2]['value'])
        value.append(i['propertiesPortion'][3]['name'])
        value.append(i['propertiesPortion'][3]['value'])
        value.append(i['propertiesPortion'][4]['name'])
        value.append(i['propertiesPortion'][4]['value'])

        dict_copm[i['materialCisNumber']]= value
        del value
        
    #with open('huawei_computer.txt', 'w') as file:
    #    for key,value in dict_copm.items():
    #        file.write(f'{key},{value}\n')
    return dict_copm

def pars_prise():

    cookies = {
    'directCrm-session': '%7B%22deviceGuid%22%3A%22b811bb12-90bf-46d1-8058-f6e0a75b4c0f%22%7D',
    'mindboxDeviceUUID': 'b811bb12-90bf-46d1-8058-f6e0a75b4c0f',
    'MVID_ENVCLOUD': 'prod1',
    'CACHE_INDICATOR': 'false',
    'COMPARISON_INDICATOR': 'false',
    'JSESSIONID': 'nWBZvXHGHyBJfpXr4DkFQyy39VxKG3svmGcT8LSV4zzS2ZJDfj1f!671526684',
    'MVID_CITY_ID': 'CityCZ_7173',
    'MVID_KLADR_ID': '3600000100000',
    'MVID_REGION_ID': '14',
    'MVID_REGION_SHOP': 'S921',
    'MVID_TIMEZONE_OFFSET': '3',
    'bIPs': '-1707567431',
    'flacktory': 'no',
    'tmr_reqNum': '20',
    'tmr_detect': '0%7C1658308156084',
    'afUserId': '9316a75c-a586-4557-9ae1-185ef9fd2a02-p',
    '_ga': 'GA1.2.247245394.1658305903',
    '_gid': 'GA1.2.1452565127.1658305903',
    'tmr_lvid': '2f9d22d3ecc41d096f4b699dd1016766',
    'tmr_lvidTS': '1658305905935',
    '_ga_BNX5WPP3YK': 'GS1.1.1658308146.2.1.1658308150.56',
    '_ga_CFMZTSS5FM': 'GS1.1.1658308146.2.1.1658308150.0',
    'MVID_CITY_CHANGED': 'false',
    'MVID_GEOLOCATION_NEEDED': 'false',
    'cookie_ip_add': '45.150.27.91',
    '__ttl__widget__ui': '1658306052607-040f688ecf58',
    'gdeslon.ru.__arc_domain': 'gdeslon.ru',
    'gdeslon.ru.user_id': 'b791052a-e0bd-4a41-9a19-44bf0039c749',
    'AF_SYNC': '1658305906677',
    'flocktory-uuid': '91ca5287-9047-43f1-8ca8-214a4ed3dd5c-1',
    'st_uid': '344642d99d71d47587cf891bed36c1fd',
    'advcake_session_id': '0390c1f0-1e9f-994b-d6fa-9f60f3d3ed5c',
    'advcake_track_id': 'd94067f8-30f8-2031-4116-d759e20d321a',
    'uxs_uid': '63e76b10-0806-11ed-8663-db5d7805e95b',
    '_ym_d': '1658305904',
    '_ym_isad': '2',
    '_ym_uid': '1658305904213173740',
    'MVID_2_exp_in_1': '1',
    'MVID_CART_AVAILABILITY': '2',
    'MVID_CREDIT_AVAILABILITY': 'true',
    'MVID_GTM_DELAY': 'true',
    'MVID_LP_SOLD_VARIANTS': '3',
    'MVID_MCLICK': 'true',
    'MVID_MOBILE_FILTERS': 'false',
    'MVID_NEW_LK': 'true',
    'MVID_NEW_LK_LOGIN': 'true',
    'MVID_SMART_BANNER_BOTTOM': 'true',
    'MVID_SUPER_FILTERS': 'true',
    '__lhash_': '8821f852021d0104116066f8c9dcac16',
    'MAIN_PAGE_VARIATION': '5',
    'MVID_ABC_TEST_WIDGET': '0',
    'MVID_AB_PROMO_DAILY': '1',
    'MVID_AB_SERVICES_DESCRIPTION': 'var2',
    'MVID_AB_TEST_COMPARE_ONBOARDING': 'true',
    'MVID_BLACK_FRIDAY_ENABLED': 'true',
    'MVID_CATALOG_STATE': '1',
    'MVID_FILTER_CODES': 'true',
    'MVID_FILTER_TOOLTIP': '1',
    'MVID_FLOCKTORY_ON': 'true',
    'MVID_GIFT_KIT': 'true',
    'MVID_IS_NEW_BR_WIDGET': 'true',
    'MVID_LAYOUT_TYPE': '1',
    'MVID_NEW_ACCESSORY': 'true',
    'MVID_NEW_DESKTOP_FILTERS': 'true',
    'MVID_NEW_LK_CHECK_CAPTCHA': 'true',
    'MVID_NEW_LK_OTP_TIMER': 'true',
    'MVID_NEW_MBONUS_BLOCK': 'true',
    'MVID_PRICE_FIRST': '2',
    'MVID_PRM20_CMS': 'true',
    'MVID_SERVICES': '111',
    'MVID_SERVICES_MINI_BLOCK': 'var2',
    'MVID_WEBP_ENABLED': 'true',
    'HINTS_FIO_COOKIE_NAME': '1',
    'MVID_ADDRESS_COMMENT_AB_TEST': '2',
    'MVID_CALC_BONUS_RUBLES_PROFIT': 'true',
    'MVID_CART_MULTI_DELETE': 'true',
    'MVID_CHECKOUT_REGISTRATION_AB_TEST': '2',
    'MVID_GET_LOCATION_BY_DADATA': 'DaData',
    'MVID_GUEST_ID': '20612185933',
    'MVID_TAXI_DELIVERY_INTERVALS_VIEW': 'new',
    'NEED_REQUIRE_APPLY_DISCOUNT': 'true',
    'PRESELECT_COURIER_DELIVERY_FOR_KBT': 'false',
    'PROMOLISTING_WITHOUT_STOCK_AB_TEST': '2',
    'searchType2': '3',
}

    headers = {
    'Accept': 'application/json',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'directCrm-session=%7B%22deviceGuid%22%3A%22b811bb12-90bf-46d1-8058-f6e0a75b4c0f%22%7D; mindboxDeviceUUID=b811bb12-90bf-46d1-8058-f6e0a75b4c0f; MVID_ENVCLOUD=prod1; CACHE_INDICATOR=false; COMPARISON_INDICATOR=false; JSESSIONID=nWBZvXHGHyBJfpXr4DkFQyy39VxKG3svmGcT8LSV4zzS2ZJDfj1f!671526684; MVID_CITY_ID=CityCZ_7173; MVID_KLADR_ID=3600000100000; MVID_REGION_ID=14; MVID_REGION_SHOP=S921; MVID_TIMEZONE_OFFSET=3; bIPs=-1707567431; flacktory=no; tmr_reqNum=20; tmr_detect=0%7C1658308156084; afUserId=9316a75c-a586-4557-9ae1-185ef9fd2a02-p; _ga=GA1.2.247245394.1658305903; _gid=GA1.2.1452565127.1658305903; tmr_lvid=2f9d22d3ecc41d096f4b699dd1016766; tmr_lvidTS=1658305905935; _ga_BNX5WPP3YK=GS1.1.1658308146.2.1.1658308150.56; _ga_CFMZTSS5FM=GS1.1.1658308146.2.1.1658308150.0; MVID_CITY_CHANGED=false; MVID_GEOLOCATION_NEEDED=false; cookie_ip_add=45.150.27.91; __ttl__widget__ui=1658306052607-040f688ecf58; gdeslon.ru.__arc_domain=gdeslon.ru; gdeslon.ru.user_id=b791052a-e0bd-4a41-9a19-44bf0039c749; AF_SYNC=1658305906677; flocktory-uuid=91ca5287-9047-43f1-8ca8-214a4ed3dd5c-1; st_uid=344642d99d71d47587cf891bed36c1fd; advcake_session_id=0390c1f0-1e9f-994b-d6fa-9f60f3d3ed5c; advcake_track_id=d94067f8-30f8-2031-4116-d759e20d321a; uxs_uid=63e76b10-0806-11ed-8663-db5d7805e95b; _ym_d=1658305904; _ym_isad=2; _ym_uid=1658305904213173740; MVID_2_exp_in_1=1; MVID_CART_AVAILABILITY=2; MVID_CREDIT_AVAILABILITY=true; MVID_GTM_DELAY=true; MVID_LP_SOLD_VARIANTS=3; MVID_MCLICK=true; MVID_MOBILE_FILTERS=false; MVID_NEW_LK=true; MVID_NEW_LK_LOGIN=true; MVID_SMART_BANNER_BOTTOM=true; MVID_SUPER_FILTERS=true; __lhash_=8821f852021d0104116066f8c9dcac16; MAIN_PAGE_VARIATION=5; MVID_ABC_TEST_WIDGET=0; MVID_AB_PROMO_DAILY=1; MVID_AB_SERVICES_DESCRIPTION=var2; MVID_AB_TEST_COMPARE_ONBOARDING=true; MVID_BLACK_FRIDAY_ENABLED=true; MVID_CATALOG_STATE=1; MVID_FILTER_CODES=true; MVID_FILTER_TOOLTIP=1; MVID_FLOCKTORY_ON=true; MVID_GIFT_KIT=true; MVID_IS_NEW_BR_WIDGET=true; MVID_LAYOUT_TYPE=1; MVID_NEW_ACCESSORY=true; MVID_NEW_DESKTOP_FILTERS=true; MVID_NEW_LK_CHECK_CAPTCHA=true; MVID_NEW_LK_OTP_TIMER=true; MVID_NEW_MBONUS_BLOCK=true; MVID_PRICE_FIRST=2; MVID_PRM20_CMS=true; MVID_SERVICES=111; MVID_SERVICES_MINI_BLOCK=var2; MVID_WEBP_ENABLED=true; HINTS_FIO_COOKIE_NAME=1; MVID_ADDRESS_COMMENT_AB_TEST=2; MVID_CALC_BONUS_RUBLES_PROFIT=true; MVID_CART_MULTI_DELETE=true; MVID_CHECKOUT_REGISTRATION_AB_TEST=2; MVID_GET_LOCATION_BY_DADATA=DaData; MVID_GUEST_ID=20612185933; MVID_TAXI_DELIVERY_INTERVALS_VIEW=new; NEED_REQUIRE_APPLY_DISCOUNT=true; PRESELECT_COURIER_DELIVERY_FOR_KBT=false; PROMOLISTING_WITHOUT_STOCK_AB_TEST=2; searchType2=3',
    'Referer': 'https://www.mvideo.ru/noutbuki-planshety-komputery-8/noutbuki-118/f/brand=huawei/tolko-v-nalichii=da/kolichestvo-yader=4,6/razreshenie-ekrana=2160x1440-piks,2560x1440-piks,2880x1800-piks,3000x2000-piks,3300x2200-piks,3840x2160-piks,3840x2400-piks?sort=price_asc',
    'Host': 'www.mvideo.ru',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Safari/605.1.15',
    'Accept-Language': 'ru',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'x-set-application-id': 'b6636c03-14c5-46f6-a816-d0647b74203d',
}

    params = {
    'productIds': '30062804,30059533,30062803,30059532,30059531,30059530,30058014,30058015',
    'addBonusRubles': 'true',
    'isPromoApplied': 'true',
}

    response = requests.get('https://www.mvideo.ru/bff/products/prices', params=params, cookies=cookies, headers=headers).json()
    price = response.get('body').get('materialPrices')
    dict_price = {}
    for i in price:
        list_price = {}
        #print(i['productId'])
        #print(i['price']['basePrice'],i['price']['salePrice'])
        #print()
        list_price['basePrice'] = i['price']['basePrice']
        list_price['salePrice'] = i['price']['salePrice']
        dict_price[i['productId']] = list_price
        del list_price

    return dict_price


for key,value in pars_prise().items():
    if key in pars_product():
        print(pars_product()[key])
        print('id: ',key,value)
        print()
     
print()