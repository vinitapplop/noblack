from volunteer.models import Country, State, City


def addCountries():
    f = open('noblack/countries.csv','r')
    lines = f.readlines()
    for line in lines:
        data = line.strip().split(',')
        # print(data)
        country = Country(country_name=data[2],country_code=data[1])
        country.save()
    return


def addStates():
    fc = open('noblack/countries.csv', 'r',encoding='utf-8')
    ls = fc.readlines()
    m = {}
    for l in ls:
        d = l.strip().split(',')
        m[d[0]] = (d[2],d[1])
    # print(m)
    f = open('noblack/states.csv', 'r',encoding='utf-8')
    lines = f.readlines()
    for line in lines:
        data = line.strip().split(',')
        # print(data)
        countryId = data[2]
        country = Country.objects.get(country_name=m[countryId][0],country_code=m[countryId][1])
        state = State(country=country, state_name=data[1], state_code=data[0])
        state.save()
    return


def addCitiesX():
    fs = open('noblack/states.csv', encoding='ISO-8859-1')
    ls = fs.readlines()
    m = {}
    for l in ls:
        d = l.strip().split(',')
        m[d[0]] = (d[1],d[2])
    # print(m)
    f = open('noblack/cities.csv','r',encoding='utf-8')
    print("line")
    lines = f.readlines()
    for line in lines:
        try:
            data = line.strip().split(',')
            stateId = data[2]
            state = State.objects.filter(state_name=m[stateId][0],state_code=stateId)
            print(state)
            if(len(state)>1):
                print(state)
            print(data[1])
            city = City(state=state[0],city_name=str(data[1]),city_code=data[0])
            city.save()
        except:
            print("wow")
    return


addCountries()
addStates()
addCitiesX()
