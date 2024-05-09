from web3 import Web3
from web3.middleware import geth_poa_middleware

import string

web3 = Web3(Web3.HTTPProvider('http://localhost:8545'))
web3.middleware_onion.inject(geth_poa_middleware, layer=0)

accounts = web3.eth.accounts
address = "0x7270701c53C3fCEcBbf25a5108882c055FF41cF1"
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
		"name": "getAllIds",
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

def authorization():
    key = input("Введите публичный ключ: ")
    password = input("Введите пароль: ")
    try:
        web3.geth.personal.unlock_account(key, password)
        print("Вы успешно вошли в аккаунт.")
        return key
    except Exception as e:
        print(e)
        return None

def withdraw(account):
    while (True):
        try:
            amount = int(input("Введите сумму для снятия: "))
            break
        except(ValueError):
            print("Введите число.")
            continue
    try:
        hash = contract.functions.withDraw(amount).transact({'from': account})
        print("Транзакция на снятие средств успешно отправлена. Хэш транзакции: ", hash.hex())
    except Exception as e:
        print("Ошибка при снятии средств: ", e)
    
def createEstate(account):
    name = str(input("Введите название недвижимости: "))
    address = str(input("Введите адрес недвижимости: "))
    print('Выберет тип недвижимости: ')
    print("1. Дом \n2. Апартамент \n3. Квартира \n4. Лофт")
    while(True):
        try:
            type = int(input("Введите тип недвижимости: "))
            break
        except (ValueError):
            print("Введите число типа.")
            continue
    while (True):
        try:
            rooms = int(input("Введите количество комнат: "))
            break
        except (ValueError):
            print("Введите число комнат.")
            continue
    description = str(input("Введите описание недвижимости: "))
    try:
        hash = contract.functions.createEstate(name, address, type, rooms, description).transact({'from': account})
        print("Транзакция на создание недвижимости отправлена успешно. Хэш транзакции: ", hash.hex())
    except Exception as e:
        print("Ошибка при создании недвижимости: ", e)

def main():
    isNotAuth = True
    auth = ''
    while True:
        if isNotAuth:
            print('1. Создать аккаунт.')
            print('2. Войти в аккаунт.')
            selection = int(input('Выберите действие: '))
            match selection:
                case 1:
                    auth = authorization()
                    if auth != None: 
                        isNotAuth = False
                case 2:
                    main()
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
                    print()
                case _:
                    print('Некорректный ввод.')



for account in accounts:
    balance = web3.eth.get_balance(account)
    print(f'Аккаунт: {account}, Баланс: {web3.from_wei(balance, "ether")} ETH')

if __name__ == "__main__":
    main()