import string
from web3.middleware import *
from web3 import Web3

web3 = Web3(Web3.HTTPProvider('http://localhost:8545'))
web3.middleware_onion.inject(geth_poa_middleware, layer=0)

accounts = web3.eth.accounts
address = '0xac951C9B7501F821D13e4d89f8386F7C1b355aE7'

abi = '''[
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"internalType": "address",
				"name": "owner",
				"type": "address"
			},
			{
				"indexed": true,
				"internalType": "uint256",
				"name": "estateID",
				"type": "uint256"
			},
			{
				"indexed": true,
				"internalType": "uint256",
				"name": "adID",
				"type": "uint256"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "date",
				"type": "uint256"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "price",
				"type": "uint256"
			}
		],
		"name": "AdCreated",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"internalType": "address",
				"name": "owner",
				"type": "address"
			},
			{
				"indexed": true,
				"internalType": "uint256",
				"name": "estateID",
				"type": "uint256"
			},
			{
				"indexed": true,
				"internalType": "uint256",
				"name": "adID",
				"type": "uint256"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "date",
				"type": "uint256"
			},
			{
				"indexed": false,
				"internalType": "enum EstateAgency.AdvertisementStatus",
				"name": "adStatus",
				"type": "uint8"
			}
		],
		"name": "AdUpdated",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"internalType": "address",
				"name": "owner",
				"type": "address"
			},
			{
				"indexed": true,
				"internalType": "uint256",
				"name": "estateID",
				"type": "uint256"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "date",
				"type": "uint256"
			},
			{
				"indexed": false,
				"internalType": "enum EstateAgency.EstateType",
				"name": "estateType",
				"type": "uint8"
			}
		],
		"name": "EstateCreated",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"internalType": "address",
				"name": "owner",
				"type": "address"
			},
			{
				"indexed": true,
				"internalType": "address",
				"name": "buyer",
				"type": "address"
			},
			{
				"indexed": true,
				"internalType": "uint256",
				"name": "adID",
				"type": "uint256"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "estateID",
				"type": "uint256"
			},
			{
				"indexed": false,
				"internalType": "enum EstateAgency.AdvertisementStatus",
				"name": "adStatus",
				"type": "uint8"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "date",
				"type": "uint256"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "price",
				"type": "uint256"
			}
		],
		"name": "EstatePurchased",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"internalType": "address",
				"name": "owner",
				"type": "address"
			},
			{
				"indexed": true,
				"internalType": "uint256",
				"name": "estateID",
				"type": "uint256"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "date",
				"type": "uint256"
			},
			{
				"indexed": false,
				"internalType": "bool",
				"name": "isActive",
				"type": "bool"
			}
		],
		"name": "EstateUpdated",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"internalType": "address",
				"name": "receiver",
				"type": "address"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "amount",
				"type": "uint256"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "date",
				"type": "uint256"
			}
		],
		"name": "FundsSent",
		"type": "event"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "advertisements",
		"outputs": [
			{
				"internalType": "address",
				"name": "owner",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "buyer",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "price",
				"type": "uint256"
			},
			{
				"internalType": "enum EstateAgency.AdvertisementStatus",
				"name": "adStatus",
				"type": "uint8"
			},
			{
				"internalType": "uint256",
				"name": "estateID",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "dateTime",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "adID",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"name": "balanceSeller",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "estateID",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "_price",
				"type": "uint256"
			}
		],
		"name": "createAd",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_name",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_addressOfEstate",
				"type": "string"
			},
			{
				"internalType": "enum EstateAgency.EstateType",
				"name": "_estateType",
				"type": "uint8"
			},
			{
				"internalType": "uint256",
				"name": "_rooms",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "_describe",
				"type": "string"
			}
		],
		"name": "createEstate",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "estates",
		"outputs": [
			{
				"internalType": "string",
				"name": "name",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "addressOfEstate",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "estateID",
				"type": "uint256"
			},
			{
				"internalType": "enum EstateAgency.EstateType",
				"name": "estateType",
				"type": "uint8"
			},
			{
				"internalType": "uint256",
				"name": "rooms",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "describe",
				"type": "string"
			},
			{
				"internalType": "address",
				"name": "owner",
				"type": "address"
			},
			{
				"internalType": "bool",
				"name": "isActive",
				"type": "bool"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "adID",
				"type": "uint256"
			}
		],
		"name": "getAd",
		"outputs": [
			{
				"components": [
					{
						"internalType": "address",
						"name": "owner",
						"type": "address"
					},
					{
						"internalType": "address",
						"name": "buyer",
						"type": "address"
					},
					{
						"internalType": "uint256",
						"name": "price",
						"type": "uint256"
					},
					{
						"internalType": "enum EstateAgency.AdvertisementStatus",
						"name": "adStatus",
						"type": "uint8"
					},
					{
						"internalType": "uint256",
						"name": "estateID",
						"type": "uint256"
					},
					{
						"internalType": "uint256",
						"name": "dateTime",
						"type": "uint256"
					},
					{
						"internalType": "uint256",
						"name": "adID",
						"type": "uint256"
					}
				],
				"internalType": "struct EstateAgency.Advertisement",
				"name": "",
				"type": "tuple"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "getAllAds",
		"outputs": [
			{
				"components": [
					{
						"internalType": "address",
						"name": "owner",
						"type": "address"
					},
					{
						"internalType": "address",
						"name": "buyer",
						"type": "address"
					},
					{
						"internalType": "uint256",
						"name": "price",
						"type": "uint256"
					},
					{
						"internalType": "enum EstateAgency.AdvertisementStatus",
						"name": "adStatus",
						"type": "uint8"
					},
					{
						"internalType": "uint256",
						"name": "estateID",
						"type": "uint256"
					},
					{
						"internalType": "uint256",
						"name": "dateTime",
						"type": "uint256"
					},
					{
						"internalType": "uint256",
						"name": "adID",
						"type": "uint256"
					}
				],
				"internalType": "struct EstateAgency.Advertisement[]",
				"name": "",
				"type": "tuple[]"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "getAllEstates",
		"outputs": [
			{
				"components": [
					{
						"internalType": "string",
						"name": "name",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "addressOfEstate",
						"type": "string"
					},
					{
						"internalType": "uint256",
						"name": "estateID",
						"type": "uint256"
					},
					{
						"internalType": "enum EstateAgency.EstateType",
						"name": "estateType",
						"type": "uint8"
					},
					{
						"internalType": "uint256",
						"name": "rooms",
						"type": "uint256"
					},
					{
						"internalType": "string",
						"name": "describe",
						"type": "string"
					},
					{
						"internalType": "address",
						"name": "owner",
						"type": "address"
					},
					{
						"internalType": "bool",
						"name": "isActive",
						"type": "bool"
					}
				],
				"internalType": "struct EstateAgency.Estate[]",
				"name": "",
				"type": "tuple[]"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "getBalance",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "estateID",
				"type": "uint256"
			}
		],
		"name": "getEstate",
		"outputs": [
			{
				"components": [
					{
						"internalType": "string",
						"name": "name",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "addressOfEstate",
						"type": "string"
					},
					{
						"internalType": "uint256",
						"name": "estateID",
						"type": "uint256"
					},
					{
						"internalType": "enum EstateAgency.EstateType",
						"name": "estateType",
						"type": "uint8"
					},
					{
						"internalType": "uint256",
						"name": "rooms",
						"type": "uint256"
					},
					{
						"internalType": "string",
						"name": "describe",
						"type": "string"
					},
					{
						"internalType": "address",
						"name": "owner",
						"type": "address"
					},
					{
						"internalType": "bool",
						"name": "isActive",
						"type": "bool"
					}
				],
				"internalType": "struct EstateAgency.Estate",
				"name": "",
				"type": "tuple"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "adID",
				"type": "uint256"
			}
		],
		"name": "purchaseEstate",
		"outputs": [],
		"stateMutability": "payable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "adID",
				"type": "uint256"
			},
			{
				"internalType": "enum EstateAgency.AdvertisementStatus",
				"name": "_adStatus",
				"type": "uint8"
			}
		],
		"name": "updateAdStatus",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "estateID",
				"type": "uint256"
			},
			{
				"internalType": "bool",
				"name": "_isActive",
				"type": "bool"
			}
		],
		"name": "updateEstateStatus",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "amount",
				"type": "uint256"
			}
		],
		"name": "withdraw",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	}
]'''

contract = web3.eth.contract(address=address, abi=abi)


def check(password):
    digits = any(char in string.digits for char in password)
    punctuation = any(char in string.punctuation for char in password)
    lowers = any(char in string.ascii_lowercase for char in password)
    capitals = any(char in string.ascii_uppercase for char in password)

    if digits and punctuation and lowers and capitals and len(password) >= 12:
        return True
    else:
        return False


def authorization():
    key = str(input('Введите публичный ключ: '))
    password = str(input('Введите пароль: '))
    try:
        web3.geth.personal.unlock_account(key, password)
        print('Вы успешно вошли в аккаунт.')
        return key
    except Exception as e:
        print(e)
        return None


def registration():
    while True:
        password = str(input('Введите пароль: '))
        if check(password):
            break
        else:
            print('Вы ввели слишком слабый пароль.')
    _add = web3.geth.personal.new_account(password)
    print(f'Адрес нового аккаунта: {_add}')


def withdraw(account):
    global amount
    while True:
        try:
            amount = int(input('Введите сумму для снятия: '))
            if amount <= 0:
                print('Сумма должна быть больше нуля.')
                continue
            break
        except ValueError:
            print('Вы ввели некорректое значение.')
            continue
    try:
        _hash = contract.functions.withdraw(amount).transact({'from': account})
        print('Транзакция на снятие средств успешно отправлена. Хэш транзакции: ', _hash.hex())
    except Exception as e:
        print(f'Ошибка при снятии средств: {e}')


def get_balance(account):
    try:
        balance = contract.functions.getBalance().call({'from': account})
        print(f'Баланс аккаунта: {balance} WEI')
    except Exception as e:
        print(f'Ошибка при получении баланса: {e}')


def create_estate(account):
    global _type, _rooms
    _name = str(input('Введите название недвижимости: '))
    _add = str(input('Введите адрес недвижимости: '))

    print('0. Дом.')
    print('1. Апартаменты.')
    print('2. Квартира.')
    print('3. Лофт.')

    while True:
        try:
            _type = int(input('Введите тип недвижимости: '))
            break
        except ValueError:
            print('Вы ввели некорректое значение.')
            continue

    while True:
        try:
            _rooms = int(input('Введите количество комнат: '))
            break
        except ValueError:
            print('Вы ввели некорректое значение.')
            continue

    description = str(input('Введите описание недвижимости: '))

    try:
        _hash = contract.functions.createEstate(_name, _add, _type, _rooms, description).transact({'from': account})
        print(f'Хэш транзакции: {_hash.hex()}')
    except Exception as e:
        print(f'Ошибка при создании недвижимости: {e}')


def create_ad(account):
    global price, _id
    try:
        ests = contract.functions.getAllEstates().call()
        print(f'Список недвижимостей: {ests}')
    except Exception as _e:
        print(f'Ошибка при выводе недвижимостей: {_e}')

    while True:
        try:
            _id = int(input('Введите ID недвижимости: '))
            break
        except ValueError:
            print('Вы ввели некорректое значение.')
            continue

    while True:
        try:
            price = int(input('Введите цену недвижимости: '))
            if price <= 0:
                print('Цена должна быть больше нуля.')
                continue
            break
        except ValueError:
            print('Вы ввели некорректое значение.')
            continue
    try:
        _hash = contract.functions.createAd(_id, price).transact({'from': account})
        print(f'Хэш транзакции: {_hash.hex()}')
    except Exception as _e:
        print(f'Ошибка при создании объявления: {_e}')


def purchase_estate(account):
    global _id
    try:
        ads = contract.functions.getAllAds().call()
        print(f'Список объявлений: {ads}')
    except Exception as e:
        print(f'Ошибка при выводе объявлений: {e}')

    while True:
        try:
            _id = int(input('Введите ID обьявления: '))
            break
        except ValueError:
            print('Вы ввели некорректое значение.')
            continue
    try:
        _hash = contract.functions.purchaseEstate(_id).transact({'from': account})
        print(f'Хэш транзакции: {_hash.hex()}')
    except Exception as _e:
        print(f'Ошибка при покупке недвижимости: {_e}')


def update_estate(account):
    global _id, _status
    try:
        ests = contract.functions.getAllEstates().call()
        print(f'Список недвижимостей: {ests}')
    except Exception as _e:
        print(f'Ошибка при выводе недвижимостей: {_e}')

    while True:
        try:
            _id = int(input('Введите ID недвижимости: '))
            break
        except ValueError:
            print('Вы ввели некорректое значение.')
            continue

    while True:
        try:
            print('Заблокировать объявление - false.')
            print('Разблокировать объявление - true.')
            _status = bool(input('Выберите действие: '))
            break
        except ValueError:
            print('Вы ввели некорректое значение.')
            continue
    try:
        _hash = contract.functions.updateEstateStatus(_id, _status).transact({'from': account})
        print(f'Хэш транзакции: {_hash.hex()}')
    except Exception as _e:
        print(f'Ошибка при обновлении статуса недвижимости: {_e}')


def update_ad(account):
    global _status, _id
    try:
        ads = contract.functions.getAllAds().call()
        print(f'Список объявлений: {ads}')
    except Exception as _e:
        print(f'Ошибка при выводе объявлений: {_e}')

    while True:
        try:
            _id = int(input('Введите ID объявления: '))
            break
        except ValueError:
            print("Такого ID нет.")
            continue

    while True:
        try:
            print('0. Открыть объявление.')
            print('1. Закрыть объявление.')
            _status = int(input('Выберите действие: '))
            break
        except ValueError:
            print('Вы ввели некорректное число!')
            continue
    try:
        _hash = contract.functions.updateAdStatus(_id, _status).transact({'from': account})
        print(f'Хэш транзакции: {_hash.hex()}')
    except Exception as e:
        print(f'Ошибка при обновлении статуса объявления: {e}')


def main():
    is_not_auth = True
    account = ''
    while True:
        try:
            if is_not_auth:
                print('1. Создать аккаунт.')
                print('2. Войти в аккаунт.')
                print('0. Завершить работу программы.')
                selection = int(input('Выберите действие: '))
                match selection:
                    case 0:
                        return
                    case 1:
                        registration()
                    case 2:
                        account = authorization()
                        if account is not None:
                            is_not_auth = False
                    case _:
                        print('Вы ввели некорректное число!')
            else:
                print('1. Купить недвижимость.')
                print('2. Создать недвижимость.')
                print('3. Создать объявление.')
                print('4. Обновить недвижимость.')
                print('5. Обновить объявление.')
                print('6. Снять средства с аккаунта.')
                print('7. Вывести баланс аккаунта.')
                print('0. Выйти')
                selection = int(input('Выберите действие: '))
                match selection:
                    case 1:
                        purchase_estate(account)
                    case 2:
                        create_estate(account)
                    case 3:
                        create_ad(account)
                    case 4:
                        update_estate(account)
                    case 5:
                        update_ad(account)
                    case 6:
                        withdraw(account)
                    case 7:
                        print(f'Баланс аккаунта: {web3.eth.get_balance(account)} WEI')
                    case 0:
                        is_not_auth = True
                    case _:
                        print('Вы ввели некорректное число!')
        except ValueError:
            print('Вы ввели некорректое значение.')


if __name__ == '__main__':
    main()
