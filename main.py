from RiotAPI import RiotAPI


def main():
    api = RiotAPI('')
    r = api.get_summoner_by_name('Finalintuitions')
    print (r)


if __name__ == '__main__':
    main()