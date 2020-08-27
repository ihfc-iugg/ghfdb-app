
from django.db.models import Avg, Count, Func, FloatField, F, Value, CharField
from django.db.models.functions import Concat
from collections import OrderedDict


class Round(Func):
    function = 'ROUND'
    template="%(function)s(%(expressions)s::numeric, 2)"

def get_db_summary(qs):

    heat_flow_sites = Count('heatflow',distinct=True)
    heat_flow_uncorrected = Count('heatflow__uncorrected', ouput_field=FloatField())
    heat_flow_corrected = Count('heatflow__corrected', ouput_field=FloatField())
    thermal_conductivity=Count('conductivity',distinct=True)
    heat_generation=Count('heatgeneration',distinct=True)
    thermal_gradient=Count('thermalgradient',distinct=True)
    temperature=Count('temperature',distinct=True)

    # Calculates information on the current Site query
    counts = qs.aggregate(
        heat_flow_sites=heat_flow_sites,
        heat_flow_uncorrected=heat_flow_uncorrected,
        heat_flow_corrected=heat_flow_corrected,
    )
    # the following counts do not play nicely with the ones above, must keep seperate and join later
    counts2 = qs.aggregate(
        thermal_conductivity=thermal_conductivity,
        heat_generation=heat_generation,
        thermal_gradient=thermal_gradient,
        temperature=temperature,
    )  
    counts.update(counts2)


    heatflow_ave = ((Avg('heatflow__uncorrected', ouput_field=FloatField()) * heat_flow_uncorrected) + (Avg('heatflow__corrected', ouput_field=FloatField()) * heat_flow_corrected)) / (heat_flow_uncorrected + heat_flow_corrected)


    # calculating averages for separate table
    ave = qs.aggregate(
        heat_flow=Round(heatflow_ave, output_field=FloatField()),     

    )

    for i in [  qs.aggregate(thermal_conductivity=Round(Avg('conductivity__value'))),
                qs.aggregate(heat_generation=Round(Avg('heatgeneration__value'))),
                qs.aggregate(thermal_gradient=Round(Avg('thermalgradient__uncorrected'))),
                qs.aggregate(temperature=Round(Avg('temperature__value'))),]:
        ave.update(i)

    return {'count': caps_dict_keys(counts),'average':caps_dict_keys(ave)}

def caps_dict_keys(my_dict):
    new_dict = {}
    for key in my_dict.keys():
        new_dict[key.replace('_',' ').title()] = my_dict[key]
    return new_dict

def Hyperlink(url, slug_field,field=None,icon=None):
    if field:
        field = F(field)
    elif icon:
        field = Value(icon)
    else:
        raise ValueError('You must specify either a field or an icon.')
    slug = F(slug_field)
    url = Value('<a href="{}'.format(url))
    return Concat(url, slug, Value('">'), field, Value("</a>"), output_field=CharField())



# AGE OPERATIONS
GEO_AGE = {

    'eon': {
            'phanerozoic':[0,541],
            'proterozoic':[541,2500],
            'archean':[2500,4000],
            'hadean':[4000,4600],
            },

    'era': {
            'cenozoic':[0,66],
            'mesozoic':[66,252.17],
            'paleozoic':[252.17,541],
            'neoproterozoic':[541,1000],
            'mesoproterozoic':[1000,1600],
            'paleoproterozoic':[1600,2500],
            'neoarchean':[2500,2800],
            'mesoarchean':[2800,3200],
            'paleoarchean':[3200,3600],
            'eoarchean':[3600,400000],
            },

    'period': {
            'quaternary':[0,2.58],
            'neogene':[2.58,23.03],
            'paleogene':[23.03,66],
            'cretaceous':[66,145],
            'jurassic':[145,201.3],
            'triassic':[201.3,252.17],
            'permian':[252.17,298.9],
            'carboniferous':[298.9,358.9],
            'devonian':[358.9,419.2],
            'silurian':[419.2,443.4],
            'ordovician':[443.4,485.4],
            'cambrian':[485.4,541],
            'ediacaran':[541,635],
            'cryogenian':[635,850],
            'tonian':[850,1000],
            'stenian':[1000,1200],
            'ecstasian':[1200,1400],
            'calymmian':[1400,1600],
            'statherian':[1600,1800],
            'orosirian':[1800,2050],
            'rhyacian':[2050,2300],
            'siderian':[2300,2500],
            },

    'epoch': {
            'holocene':[0,0.0117],
            'pleistocene':[0.0117,2.58],
            'pliocene':[2.58,5.333],
            'miocene':[5.333,23.03],
            'oligocene':[23.03,33.9],
            'eocene':[33.9,56],
            'paleocene':[56,66],
            'late-cretaceous':[66,100.5],
            'early-cretaceous':[100.5,152.1],
            'late-jurassic':[152.1,163.5],
            'middle-jurassic':[163.5,174.1],
            'early-jurassic':[174.1,201.3],
            'late-triassic':[201.3,237],
            'middle-triassic':[237,247.2],
            'early-triassic':[247.2,252.17],
            'lopingian':[252.17,259.8],
            'guadalupian':[259.8,272.3],
            'cisuralian':[272.3,298.9],
            'pennsylvanian':[298.9,323.2],
            'mississippian':[323.2,358.9],
            'late-devonian':[358.9,382.7],
            'middle-devonian':[382.7,393.3],
            'early-devonian':[393.3,419.2],
            'pridoli':[419.2,423],
            'ludlow':[423,427.4],
            'wenlock':[427.4,433.4],
            'llandovery':[433.4,443.4],
            'late-ordovician':[443.4,458.4],
            'middle-ordovician':[458.4,470],
            'early-ordovician':[470,485.4],
            'furongian':[485.4,497],
            'miaolingian':[497,509],
            'series 2':[509,521],
            'terreneuvian':[521,541],
            },

    'age': {

        'meghalayan':[0,0.0042],
        'northgrippian':[0.0042,0.0082],
        'greenlandian':[0.0082,0.0117],
        'late-pleistocene':[0.0117,0.126],
        'tarantian':[0.0117,0.126],
        'middle-pleistocene':[0.126,0.781],
        'ionian':[0.126,0.781],
        'chibanian':[0.126,0.781],
        'calabrian':[0.781,1.8],
        'gelasian':[1.8,2.58],
        'piacenzian':[2.58,3.6],
        'zanclean':[3.6,5.333],
        'messinian':[5.333,7.246],
        'tortonian':[7.246,11.63],
        'serravallian':[11.63,13.82],
        'langhian':[13.82,15.97],
        'burdigalian':[15.97,20.44],
        'aquitanian':[20.44,23.03],
        'chattian':[23.03,28.1],
        'rupelian':[28.1,33.9],
        'priabonian':[33.9,37.8],
        'bartonian':[37.8,41.2],
        'lutetian':[41.2,47.8],
        'ypresian':[47.8,56],
        'thanetian':[56,59.2],
        'selandian':[59.2,61.6],
        'danian':[61.6,66],
        'maastrichtian':[66,72.1],
        'campanian':[72.1,83.6],
        'santonian':[83.6,86.3],
        'coniacian':[86.3,89.8],
        'turonian':[89.8,93.9],
        'cenomanian':[93.9,100.5],
        'albian':[100.5,113],
        'aptian':[113,125],
        'barremian':[125,129.4],
        'hauterivian':[129.4,132.9],
        'valanginian':[132.9,139.8],
        'berriasian':[139.8,145],
        'tithonian':[145,152.1],
        'kimmeridgian':[152.1,157.3],
        'oxfordian':[157.3,163.5],
        'callovian':[163.5,166.1],
        'bathonian':[166.1,168.3],
        'bajocian':[168.3,170.3],
        'aalenian':[170.3,174.1],
        'toarcian':[174.1,182.7],
        'pliensbachian':[182.7,190.8],
        'sinemurian':[190.8,199.3],
        'hettangian':[199.3,201.3],
        'rhaetian':[201.3,208.5],
        'norian':[208.5,227],
        'carnian':[227,237],
        'ladinian':[237,242],
        'anisian':[242,247.2],
        'olenekian':[247.2,251.2],
        'induan':[251.2,251.902],
        'changhsingian':[251.902,254.14],
        'wuchiapingian':[254.14,259.1],
        'capitanian':[259.1,265.1],
        'wordian':[265.1,268.8],
        'roadian':[268.8,272.95],
        'kungurian':[272.95,283.5],
        'artinskian':[283.5,290.1],
        'sakmarian':[290.1,295],
        'asselian':[295,298.9],
        'gzhelian':[298.9,303.7],
        'kasimovian':[303.7,307],
        'moscovian':[307,315.2],
        'bashkirian':[315.2,323.2],
        'serpukhovian':[323.2,330.9],
        'viséan':[330.9,346.7],
        'tournaisian':[346.7,358.9],
        'famennian':[358.9,372.2],
        'frasnian':[372.2,382.7],
        'givetian':[382.7,387.7],
        'eifelian':[387.7,393.3],
        'emsian':[393.3,407.6],
        'pragian':[407.6,410.8],
        'lochkovian':[410.8,419.2],
        # '':[419.2,423],
        'ludfordian':[423,425.6],
        'gorstian':[425.6,427.4],
        'homerian':[427.4,430.5],
        'sheinwoodian':[430.5,433.4],
        'telychian':[433.4,438.5],
        'aeronian':[438.5,440.8],
        'rhuddanian':[440.8,443.8],
        'hirnantian':[443.8,445.2],
        'katian':[445.2,453],
        'sandbian':[453,458.4],
        'darriwilian':[458.4,467.3],
        'dapingian':[467.3,470],
        'floian':[470,477.7],
        '(formerly arenig)':[477.7,],
        'tremadocian':[0,485.4],
        'stage 10':[485.4,489.5],
        'jiangshanian':[489.5,494],
        'paibian':[494,497],
        'guzhangian':[497,500.5],
        'drumian':[500.5,504.5],
        'wuliuan':[504.5,509],
        'stage 4':[509,514],
        'stage 3':[514,521],
        'stage 2':[521,529],
        'fortunian':[529,541],
        }

    }

GEO_AGE_UNOFFICIAL = {

    # contains both official and unofficial. used to search unoffical only.
    'early-tertiary':[23.03,66],
    'late-tertiary':[1.806,23.03],
    'aalenian':[171.6,175.6],
    'abereiddian':[464,471.8],
    'acadian':[501,513],
    'actonian':[453,454],
    'adelaidean':[542,1300],
    'aegean':[243,245],
    'aeronian':[436,439],
    'aksayan':[491.5,493],
    'aktastinian':[275.6,284.4],
    'alaunian':[211,216],
    'albertan':[501,513],
    'albian':[99.6,112],
    'aldingian':[33,36],
    'alexandrian':[436,443.7],
    'alportian':[318.1,324.5],
    'altonian':[16.5,17.5],
    'amgan':[502,513],
    'animikean':[1400,2225],
    'anisian':[237,245],
    'aphebian':[1600,2500],
    'aptian':[112,125],
    'aquitanian':[20.43,23.03],
    'aratauran':[188,199.6],
    'archean':[2500,3800],
    'archeozoic':[2500,3800],
    'arenig':[471.8,478.6],
    'arenigian':[471.8,478.6],
    'arikareean':[19,30.5],
    'aritan':[125,136.4],
    'arnsbergian':[325,326],
    'arowhanan':[93,95],
    'artinskian':[275.6,284.4],
    'arundian':[339,341],
    'asbian':[333,337.5],
    'ashgill':[443.7,449],
    'asselian':[294.6,299],
    'astian':[2.588,3.6],
    'atdabanian':[524,530],
    'atokan/derryan':[308,311.7],
    'atokan':[308,311.7],
    'aurelucian':[457,460.9],
    'austinian':[65.5,99.6],
    'auversian':[37.2,40.4],
    'awamoan':[17.5,20],
    'ayusokkanian':[494.5,501],
    'azoic':[3800,4567.17],
    'baigendzinian':[275.6,284.4],
    'bairnsdalian':[10.5,15],
    'baishaean':[429,433],
    'bajocian':[167.7,171.6],
    'bala':[443.7,460.9],
    'balan':[443.7,460.9],
    'balcombian':[15,15.5],
    'bananian':[219,228],
    'baotan':[454.5,460.9],
    'barremian':[125,130],
    'barstovian':[11.8,15.5],
    'bartonian':[37.2,40.4],
    'bashkirian':[311.7,318.1],
    'basin-groups':[3975,4150],
    'batesfordian':[15.5,16.5],
    'bathonian':[164.7,167.7],
    'batyrbayan':[488.3,491.5],
    'begudian':[68,70.6],
    'bendigonian':[473,475],
    'berriasian':[140.2,145.5],
    'bithynian':[241,243],
    'black-riveran':[459,460.9],
    'blackriveran':[459,460.9],
    'blackriverian':[459,460.9],
    'blancan':[1.806,4.75],
    'bolindian':[443.7,450],
    'bolsovian':[306.5,311.7],
    'boomerangian':[501,504],
    'bortonian':[40,44],
    'botomian':[518.5,524],
    'braxtonian':[260.4,270.6],
    'bridgerian':[45.4,50.5],
    'brigantian':[326.4,336],
    'bulitian':[53,55.8],
    'buntsandstein':[245,251],
    'burdigalian':[15.97,20.43],
    'burrellian':[455,457],
    'burzyan':[1375,1400],
    'caerfai':[513,542],
    'calabrian':[0.781,1.806],
    'callovian':[161.2,164.7],
    'calymmian':[1400,1600],
    'cambrian':[488.3,542],
    'campanian':[70.6,83.5],
    'canadaway':[359.2,374.5],
    'canadian':[471.8,488.3],
    'cantabrian':[305,306.5],
    'capitanian':[260.4,265.8],
    'caradoc':[449,460.9],
    'caradocian':[449,460.9],
    'carboniferous':[299,359.2],
    'carnian':[216.5,228],
    'carpentarian':[1300,1800],
    'cassinian':[471.8,473],
    'castile':[253.8,260.4],
    'castlecliffian':[0.01143,1.1],
    'castlemanian':[470,471],
    'cautleyan':[446.5,447.5],
    'cayugan':[416,421.3],
    'cazenovian':[385.3,397.5],
    'cenomanian':[93.5,99.6],
    'cenozoic':[-0.000055012,65.5],
    'chadian':[341,345.3],
    'chadronian':[33.5,37],
    'chamovnicheskian':[305,306],
    'changhsingian':[251,253.8],
    'changlangpuan':[518,523],
    'changshanian':[492.5,496.8],
    'changshingian':[251,253.8],
    'changxingian':[251,253.8],
    'charmouthian':[183,189.6],
    'chatauquan':[359.2,370],
    'chattian':[23.03,28.4],
    'chazyan':[460.9,464],
    'cheltenhamian':[4.3,5],
    'cheneyan':[452,455],
    'cheremshanskian':[313.4,314.5],
    'chesterian':[318.1,333],
    'chewtonian':[471,473],
    'chickasawhayan':[23.03,28.4],
    'chokerian':[324.5,325],
    'chokierian':[324.5,325],
    'chouteau':[348,359.2],
    'cincinnatian':[443.7,451],
    'cisuralian':[270.6,299],
    'clairbornean':[33.9,55.8],
    'clarendonian':[9,11.8],
    'clarkforkian':[55.5,56],
    'cliffdenian':[15,16.5],
    'coahulian':[127,145.5],
    'comanchean':[99.6,127],
    'conewangan':[359.2,374.5],
    'coniacian':[85.8,89.3],
    'conneautan':[359.2,374.5],
    'costonian':[459,460.9],
    'courceyan':[345.3,359.2],
    'cressagian':[486,488.3],
    'cretaceous':[65.5,145.5],
    'croixian':[488.3,501],
    'cryogenian':[630,850],
    'cryptic':[4150,4567.17],
    'cryptozoic':[542,4567.17],
    'dacian':[3.6,5.332],
    'dalanian':[310,313],
    'danian':[61.7,65.5],
    'darriwilian':[460.9,468.1],
    'datangian':[333,345],
    'datsonian':[485,488.3],
    'dawanian':[471.8,472],
    'deer-parkian':[397.5,407],
    'delamaran':[504,512],
    'delmontian':[2.9,7.5],
    'demingian':[475,478.6],
    'derryan':[308,311.7],
    'desmoinesian':[306.5,308],
    'desmoinian':[306.5,308],
    'devonian':[359.2,416],
    'dewey-lake':[251,253.8],
    'dewuan':[318.1,333],
    'dienerian':[249.7,250.4],
    'dinantian':[326.4,359.2],
    'djulfian':[253.8,260.4],
    'dogger':[161.2,175.6],
    'dolgellian':[488.3,492.5],
    'dongganglingian':[385.3,391.4],
    'dorashamian':[251,253.8],
    'dorogomilovksian':[303.9,305],
    'dresbachian':[496.8,501],
    'dreussian':[161.2,164.7],
    'duchesnean':[37,40],
    'duckmantian':[311.7,313.4],
    'duntroonian':[27,28],
    'durango':[99.6,145.5],
    'dyeran':[512,524.5],
    'dyfed':[460.9,471.8],
    'dzhulfian':[253.8,260.4],
    'early-fordian':[65.5,99.6],
    'early-cambrian':[513,542],
    'early-carboniferous':[318.1,359.2],
    'early-cretaceous':[99.6,145.5],
    'early-devonian':[397.5,416],
    'early-eocene':[48.6,55.8],
    'early-imbrian':[3800,3900],
    'early-jurassic':[175.6,199.6],
    'early-miocene':[15.97,23.03],
    'early-mississippian':[345.3,359.2],
    'early-oligocene':[28.4,33.9],
    'early-ordovician':[471.8,488.3],
    'early-paleocene':[61.7,65.5],
    'early-pennsylvanian':[311.7,318.1],
    'early-permian':[270.6,299],
    'early-pleistocene':[0.781,1.806],
    'early-pliocene':[3.6,5.332],
    'early-silurian':[422.9,443.7],
    'early-triassic':[245,251],
    'eastonian':[450,456],
    'ectasian':[1200,1400],
    'edenian':[449,454],
    'ediacaran':[542,630],
    'ediacarian':[542,630],
    'eifelian':[391.8,397.5],
    'eildonian':[428.2,433],
    'ellesmerian':[250.4,251],
    'elvirian':[324.5,326],
    'emsian':[397.5,407],
    'eoarchean':[3600,3800],
    'eocene':[33.9,55.8],
    'erian':[388,391.8],
    'erqiaoan':[199.6,209],
    'etalian':[232,243],
    'falangian':[228,237],
    'famennian':[359.2,374.5],
    'fassanian':[231.4,237],
    'feixianguanian':[249.7,251],
    'fengshanian':[488.3,492.5],
    'fennian':[471.8,473.5],
    'festiniogian':[492.5,496.8],
    'filippovian':[270.6,275.6],
    'florian':[506,508],
    'franconian':[492.5,496.8],
    'frasnian':[374.5,385.3],
    'frederiksbergian':[99.6,112],
    'fronian':[436,437.5],
    'fujian':[9.5,11.1],
    'fupingan':[2600,3100],
    'furongian':[488.3,501],
    'fuvelian':[70.6,77],
    'gallic':[89.3,130],
    'gamachian':[443.7,445.6],
    'gangetian':[250.4,251],
    'gasconadian':[478.6,488.3],
    'gasperian':[326.4,336],
    'gault':[99.6,112],
    'gedinnian':[411.2,416],
    'gelasian':[1.806,2.588],
    'geneseean':[385.3,391.8],
    'geneyan':[452,455],
    'georgian':[513,542],
    'gisbornian':[456,460.9],
    'givetian':[385.3,391.8],
    'gleedonian':[422.9,425.4],
    'gorstian':[421.3,422.9],
    'griesbachian':[250.4,251],
    'guadalupian':[260.4,270.6],
    'guandian':[422,425.5],
    'guanlingian':[237,245],
    'gulfian':[65.5,99.6],
    'guniutanian':[464,471.8],
    'gushanian':[496.8,501],
    'gyliakian':[89.3,96.6],
    'gzelian':[299,303.9],
    'gzhelian':[299,303.9],
    'hadean':[3800,4567.17],
    'hadrynian':[542,850],
    'hallian':[-0.000055012,0.01143],
    'haranoyan':[15.97,18.2],
    'harnagian':[458,459],
    'hastarian':[348,359.2],
    'haumurian':[65.5,70.6],
    'hauterivian':[130,136.4],
    'hawera':[-0.000055012,0.01143],
    'heersian':[55.8,58.7],
    'helderbergian':[397.5,416],
    'helikian':[850,1600],
    'hemingfordian':[15.5,19],
    'hemphillian':[4.75,9],
    'heretaungan':[47,50],
    'heterian':[152,156],
    'hetonian':[65.5,77.1],
    'hettangian':[196.5,199.6],
    'hirnantian':[443.7,445.6],
    'holkerian':[337.5,339],
    'holocene':[-0.000055012,0.01143],
    'homerian':[422.9,426.2],
    'honghuayuanian':[472,478.6],
    'huashibanian':[313,318.1],
    'huobachengian':[209,219],
    'huronian':[1400,2500],
    'hutchinsonian':[20,21],
    'ibexian':[471.8,491],
    'idamean':[494,497],
    'idwian':[437.5,439],
    'illyrian':[237,239],
    'induan':[249.7,251],
    'ionian':[0.126,0.781],
    'irenian':[270.6,275.6],
    'irvingtonian':[0.3,1.806],
    'isuan':[3500,3800],
    'ivorean':[345.3,348],
    'jacksonian':[33.9,37.2],
    'janjukian':[27.5,30],
    'jeffersonian':[473,475],
    'jinningian':[800,1750],
    'johannian':[36,52],
    'julian':[225,228],
    'jurassic':[145.5,199.6],
    'kaburan':[11.1,13.5],
    'kaihikuan':[225,232],
    'kalimnan':[3.4,4.3],
    'kapitean':[4.8,6],
    'karatau':[800,1100],
    'kashirskian':[308,309.2],
    'kasimovian':[303.9,306.5],
    'kazanian':[260.4,270.6],
    'kechienjian':[1.5,1.9],
    'keiloran':[433,443.7],
    'keuper':[199.6,228],
    'kiaitan':[37.2,40],
    'kimmeridgian':[150.8,155.7],
    'kinderhookian':[348,359.2],
    'kinderscoutian':[317,318.1],
    'kirkfield':[457,458],
    'klazminskian':[300.5,303.9],
    'kochian':[136.4,145.5],
    'korangian':[110,119],
    'krevyakinskian':[306,306.5],
    'krumaian':[294.6,299],
    'kungurian':[270.6,275.6],
    'lacinian':[216,216.5],
    'ladinian':[228,237],
    'lancefieldian':[475,482],
    'landenian':[55.8,58.7],
    'langhian':[13.65,15.97],
    'langsettian':[313.4,314.5],
    'late-cambrian':[488.3,501],
    'late-carboniferous':[299,318.1],
    'late-cretaceous':[65.5,99.6],
    'late-devonian':[359.2,385.3],
    'late-eocene':[33.9,37.2],
    'late-jurassic':[145.5,161.2],
    'late-miocene':[5.332,11.608],
    'late-mississippian':[318.1,326.4],
    'late-oligocene':[23.03,28.4],
    'late-ordovician':[443.7,460.9],
    'late-paleocene':[55.8,58.7],
    'late-pennsylvanian':[299,306.5],
    'late-permian':[251,260.4],
    'late-pleistocene':[0.01143,0.126],
    'late-pliocene':[1.806,3.6],
    'late-silurian':[416,422.9],
    'late-triassic':[199.6,228],
    'latdorfian':[28.4,33.9],
    'lenian':[513,524],
    'leonardian':[270.6,280],
    'lianghekouan':[478.6,488.3],
    'lianhuashanian':[413,416],
    'lias':[175.6,199.6],
    'lillburnian':[11.5,15],
    'linxiangian':[449,454.5],
    'llandeilian':[460.9,464],
    'llandeilo':[460.9,464],
    'llandovery':[428.2,443.7],
    'llanvirn':[464,471.8],
    'llanvirnian':[464,471.8],
    'lochkovian':[411.2,416],
    'lockportian':[422.9,426.2],
    'longfordian':[16.5,27.5],
    'longmaxian':[438,443.7],
    'longobardian':[228,231.4],
    'longtanian':[253.8,260.4],
    'longvillian':[455,457],
    'longwangmioan':[513,518],
    'lopingian':[251,260.4],
    'lotharingian':[189.6,193.3],
    'lower-cambrian':[513,542],
    'lower-carboniferous':[318.1,359.2],
    'lower-cretaceous':[99.6,145.5],
    'lower-devonian':[397.5,416],
    'lower-eocene':[48.6,55.8],
    'lower-jurassic':[175.6,199.6],
    'lower-miocene':[15.97,23.03],
    'lower-mississipian':[345.3,359.2],
    'lower-oligocene':[28.4,33.9],
    'lower-ordovician':[471.8,488.3],
    'lower-paleocene':[61.7,65.5],
    'lower-pennsylvanian':[311.7,318.1],
    'lower-permian':[270.6,299],
    'lower-pleistocene':[0.781,1.806],
    'lower-pliocene':[3.6,5.332],
    'lower-silurian':[422.9,443.7],
    'lower-triassic':[245,251],
    'ludfordian':[418.7,421.3],
    'ludlow':[418.7,422.9],
    'luisian':[13.5,15.5],
    'luliangian':[1750,2350],
    'lutetian':[40.4,48.6],
    'maastrichtian':[65.5,70.6],
    'maentwrogian':[496.8,501],
    'maestrichtian':[65.5,70.6],
    'makabewan':[251,253.8],
    'malakovian':[243,248],
    'malm':[145.5,161.2],
    'mangaorapan':[50,52],
    'mangaotanean':[87,93],
    'mangapanian':[1.96,2.6],
    'mangapirian':[270.6,278],
    'maokovian':[260.4,270.6],
    'maozhangian':[509,513],
    'mapingian':[299,310],
    'marjuman':[494.5,504],
    'marsdenian':[315.5,317],
    'marshbrookian':[454,455],
    'mayan':[501,502],
    'mayvillian':[447.5,453],
    'medinan':[438,443.7],
    'meishuchuan':[532,542],
    'melbournian':[416,428.2],
    'melekesskian':[311.7,313.4],
    'menevian':[501,502],
    'meramecian':[333,340],
    'merioneth':[488.3,501],
    'mesoarchean':[2800,3200],
    'mesoproterozoic':[1000,1600],
    'mesozoic':[65.5,251],
    'messinian':[5.332,7.246],
    'miaogoalingian':[418.7,422],
    'miaopoan':[460.9,464],
    'middle-cambrian':[501,513],
    'middle-devonian':[385.3,397.5],
    'middle-eocene':[37.2,48.6],
    'middle-jurassic':[161.2,175.6],
    'middle-miocene':[11.608,15.97],
    'middle-mississippian':[326.4,345.3],
    'middle-ordovician':[460.9,471.8],
    'middle-paleocene':[58.7,61.7],
    'middle-pennsylvanian':[306.5,311.7],
    'middle-permian':[260.4,270.6],
    'middle-pleistocene':[0.126,0.781],
    'middle-triassic':[228,245],
    'midwayan':[23.03,33.9],
    'migneintian':[478.6,486],
    'mindyallan':[497,501],
    'miocene':[5.332,23.03],
    'mississippian':[318.1,359.2],
    'missourian':[305,306.5],
    'mitchellian':[5,10.5],
    'miyakoan':[96.6,125],
    'mohawkian':[451,462],
    'mohnian':[7.5,13.5],
    'mokoiwian':[119,145.5],
    'mokolian':[900,2050],
    'montezuman':[524.5,529.5],
    'montian':[61.7,65.5],
    'moridunian':[475,478.6],
    'morrisonian':[145.5,161.2],
    'morrowan':[311.7,318.1],
    'mortesnes':[630,640],
    'moscovian':[306.5,311.7],
    'motuan':[99.6,104],
    'muschelkalk':[228,245],
    'myachkovskian':[306.5,307.2],
    'nagaolingian':[410,413],
    'namibian':[542,900],
    'nammalian':[247.4,249.7],
    'namurian':[315,326.4],
    'narizian':[35,48],
    'navarroan':[65.5,70.6],
    'nectarian':[3900,3975],
    'nemakit-daldynian':[534,542],
    'neoarchean':[2500,2800],
    'neocomian':[130,145.5],
    'neogene':[-0.000055012,23.03],
    'neoproterozoic':[542,1000],
    'neoproterozoic-iii':[542,630],
    'ngaterian':[95,99.6],
    'niagaran':[421.3,438],
    'noginskian':[299,300.5],
    'norian':[203.6,216.5],
    'nuevo-leonian':[89.3,130],
    'nukumaruan':[1.1,1.96],
    'nullaginian':[1800,2500],
    'ochoan':[251,260.4],
    'ohauan':[150,152],
    'okehuan':[0.48,1.1],
    'olenekian':[245,249.7],
    'oligocene':[23.03,33.9],
    'onnian':[449,453],
    'ontarian':[428.2,436],
    'opoitian':[3.6,4.8],
    'ordian':[510,520],
    'ordovician-ii':[471.8,478.6],
    'ordovician-iii':[468.1,471.8],
    'ordovician-v':[455.8,460.9],
    'ordovician-vi':[445.6,455.8],
    'ordovician':[443.7,488.3],
    'orellan':[32,33.5],
    'oretian':[218,225],
    'orosirian':[1800,2050],
    'osagean':[340,348],
    'otaian':[21,23.03],
    'otamitan':[206,218],
    'otapirian':[199.6,203],
    'oxfordian':[155.7,161.2],
    'paibian':[496,501],
    'paleoarchean':[3200,3600],
    'paleocene':[55.8,65.5],
    'paleogene':[23.03,65.5],
    'paleoproterozoic':[1600,2500],
    'paleozoic':[251,542],
    'payntonian':[488.3,491],
    'pelsonian':[239,241],
    'pendleian':[326,326.4],
    'penglaizhenian':[145.5,149],
    'pennsylvanian':[299,318.1],
    'penutian':[51,53],
    'permian':[251,299],
    'phanerozoic':[-0.000055012,542],
    'piacenzian':[2.588,3.6],
    'piripauan':[70.6,83.5],
    'pleistocene':[0.01143,1.806],
    'pleistogene':[-0.000055012,1.806],
    'pliensbachian':[183,189.6],
    'pliocene':[1.806,5.332],
    'podolskian':[307.2,308],
    'porangan':[44,47],
    'portlandian':[142,146],
    'potsdamian':[488.3,501],
    'poundian':[542,570],
    'praghian':[407,411.2],
    'precambrian':[542,4567.17],
    'priabonian':[33.9,37.2],
    'pridoli':[416,418.7],
    'primary':[251,542],
    'primordial':[542,4567.17],
    'priscoan':[3800,4567.17],
    'proterozoic':[542,2500],
    'puaroan':[145.5,150],
    'puercan':[62.5,65.5],
    'puruhuahuaun':[253.8,260.4],
    'pusgillian':[447.5,449],
    'putikian':[0.01143,0.48],
    'qianxin':[3400,3800],
    'quaternary':[-0.000055012,1.806],
    'qungzusian':[523,532],
    'rancholabrean':[0.01143,0.3],
    'randian':[2500,3000],
    'rawtheyan':[445.6,446.5],
    'recent':[-0.000055012,0.01143],
    'redonian':[2.588,3.6],
    'refugian':[33.5,35],
    'relizian':[15.5,16.5],
    'repettian':[2.2,2.9],
    'rhaetian':[199.6,203.6],
    'rhuddanian':[439,443.7],
    'rhyacian':[2050,2300],
    'richmondian':[445.6,449],
    'riphean':[800,1400],
    'roadian':[268,270.6],
    'rocklandian':[458,459],
    'rognacian':[65.5,68],
    'romanian':[2.588,3.6],
    'rotliegendes':[270.6,299],
    'runangan':[33.9,37.2],
    'rupelian':[28.4,33.9],
    'rustlerian':[253.8,260.4],
    'ryzanian':[136.5,142],
    'saint-david\'s':[501,513],
    'saint-geneviere':[326.4,336],
    'sakian':[493,494.5],
    'sakmarian':[284.4,294.6],
    'saladoan':[253.8,260.4],
    'salem':[337.5,339],
    'santonian':[83.5,85.8],
    'saucesian':[16.5,22],
    'sawkillian':[397.5,407],
    'scythian':[245,251],
    'secondary':[65.5,251],
    'selandian':[58.7,61.7],
    'senecan':[370,388],
    'senonian':[65.5,89.3],
    'serpukhovian':[318.1,326.4],
    'serravallian':[11.608,13.65],
    'sevatian':[203.6,211],
    'shaodongian':[349.5,359.2],
    'shaximioan':[161.2,167],
    'sheinwoodian':[426.2,428.2],
    'shermanian':[454,457],
    'shetianqiaoan':[374.5,385.3],
    'shinulanian':[433,438],
    'sicilian':[0.26,0.781],
    'siderian':[2300,2500],
    'siegenian':[407,411.2],
    'silesian':[299,326.4],
    'silurian':[416,443.7],
    'sinemurian':[189.6,196.5],
    'sinian':[542,800],
    'sipaian':[397.5,407],
    'smalfjord':[640,650],
    'smithian':[247.4,249.7],
    'solvan':[502,513],
    'sonyean':[374.5,385.3],
    'soudleyan':[457,458],
    'southwoodian':[391.8,397.5],
    'spathian':[245,247.4],
    'st.david\'s':[501,513],
    'st.geneviere':[326.4,336],
    'stampian':[28.4,33.9],
    'statherian':[1600,1800],
    'stenian':[1000,1200],
    'stephanian':[299,306.5],
    'steptoan':[493,494.5],
    'sterlitamakian':[284.4,294.6],
    'streffordian':[449,452],
    'sturtian':[650,800],
    'suchian':[1.9,3],
    'suiningian':[149,161.2],
    'sunwaptan':[491,493],
    'surenian':[294.6,299],
    'swazian':[3000,4000],
    'tabianian':[3.6,5.332],
    'taghanican':[385.3,391.8],
    'tarantian':[0.01143,0.126],
    'tastubian':[284.4,294.6],
    'tatarian':[251,260.4],
    'taylorian':[70.6,83.5],
    'telfordian':[278,289],
    'telychian':[428.2,436],
    'temaikan':[161.2,169],
    'templetonian':[508,510],
    'teratan':[83.5,87],
    'tertiary':[1.806,65.5],
    'teurian':[56.5,65.5],
    'thanetian':[55.8,58.7],
    'thuringian':[251,270.6],
    'tiffanian':[56,60.5],
    'tioughniogan':[385.3,391.8],
    'tithonian':[145.5,150.8],
    'toarcian':[175.6,183],
    'tommotian':[530,534],
    'tonawandian':[426.2,428.2],
    'tongaporutuan':[6,10],
    'tongrian':[28.4,33.9],
    'tonian':[850,1000],
    'torrejonian':[60.5,62.5],
    'tortonian':[7.246,11.608],
    'totomian':[3,3.6],
    'tournaisian':[345.3,359.2],
    'toyonian':[513,518.5],
    'tozawan':[13.5,15.97],
    'tremadoc':[478.6,488.3],
    'tremadocian':[478.6,488.3],
    'trempealeauan':[488.3,492.5],
    'trentonian':[449,460.9],
    'triassic':[199.6,251],
    'trinitian':[89.3,130],
    'turonian':[89.3,93.5],
    'tuvalian':[216.5,225],
    'tyrrhenian':[0.01143,0.26],
    'ufimian':[268,270.6],
    'uintan':[40,45.4],
    'ulatisian':[48,51],
    'ulsterian':[391.8,416],
    'undillian':[504,506],
    'upper-cambrian':[488.3,501],
    'upper-carboniferous':[299,318.1],
    'upper-cretaceous':[65.5,99.6],
    'upper-devonian':[359.2,385.3],
    'upper-eocene':[33.9,37.2],
    'upper-jurassic':[145.5,161.2],
    'upper-miocene':[5.332,11.608],
    'upper-mississippian':[318.1,326.4],
    'upper-oligocene':[23.03,28.4],
    'upper-ordovician':[443.7,460.9],
    'upper-paleocene':[55.8,58.7],
    'upper-pennsylvanian':[299,306.5],
    'upper-permian':[251,260.4],
    'upper-pleistocene':[0.01143,0.126],
    'upper-pliocene':[1.806,3.6],
    'upper-silurian':[416,422.9],
    'upper-triassic':[199.6,228],
    'urakawan':[77.1,89.3],
    'urgonian':[112,125],
    'uruoan':[169,188],
    'urutawan':[104,110],
    'uskalikian':[294.6,299],
    'vaalian':[2050,2500],
    'valanginian':[136.4,140.2],
    'valdonnian':[77,83.5],
    'varanger':[630,650],
    'varangian':[630,650],
    'vendian':[542,650],
    'venturian':[1.9,2.2],
    'vereiskian':[309.2,311.7],
    'vicksburgian':[28.4,33.9],
    'virgilian':[299,305],
    'visean':[326.4,345.3],
    'volgian':[142,150.8],
    'waiauan':[10,11.5],
    'waiitian':[253.8,260.4],
    'waipawan':[52,56.5],
    'waipipian':[2.6,3.6],
    'waitakian':[23.03,27],
    'waltonian':[1.806,2.588],
    'wangerripian':[52,61.7],
    'warendian/lancefieldian':[475,485],
    'warendian':[478.6,485],
    'warepan':[203,206],
    'warsaw':[339,341],
    'wasatchian':[50.5,55.5],
    'waucoban':[513,542],
    'wenlock':[422.9,428.2],
    'werrikooian':[1,1.806],
    'west-fallsian':[374.5,385.3],
    'westphalian':[304,313],
    'whaingaroan':[28,33.9],
    'wheelerian':[0.01143,1.9],
    'white-rockian':[462,471.8],
    'whitlandian':[473.5,475],
    'whitneyan':[30.5,32],
    'whitwellian':[425.4,426.2],
    'wolfcampian':[280,299],
    'wonokan':[570,630],
    'woodbinian':[93.5,99.6],
    'wordian':[265.8,268],
    'wuchiapingian':[253.8,260.4],
    'wufengian':[443.7,449],
    'wujiapingian':[253.8,260.4],
    'wutaian':[2350,2600],
    'xikuangshanian':[359.2,374.5],
    'xintiangouan':[167,175.6],
    'xiushanian':[425.5,429],
    'xixianian':[270.6,299],
    'yanguan':[345,349.5],
    'yatalan':[2,3.4],
    'yeadonian':[314.5,315.5],
    'yingtangian':[391.4,397.5],
    'ynezian':[55.8,61.5],
    'yongningzhenian':[245,249.7],
    'ypeenian':[468.1,470],
    'ypresian':[48.6,55.8],
    'yuian':[3.6,9.5],
    'yujianian':[407,410],
    'yulongsian':[416,418.7],
    'yurmatian':[1100,1375],
    'yuzanjian':[0.75,1.5],
    'zanclean':[3.6,5.332],
    'zanclian':[3.6,5.332],
    'zechstein':[251,260.4],
    'zemorrian':[22,33.5],
    'zhungxian':[501,505],
    'ziliujingian':[175.6,199.6],
    'zuzhuangian':[505,509],
}

def _age_lookup(age,lookup_dict):
    return next(key for key, value in lookup_dict.items() if value[0] <= age < value[1])

def _geo_age_lookup(geo_age):

    for i in GEO_AGE.values():
        try:
            return tuple(next(value for key, value in i.items() if key == geo_age))
        except StopIteration:
            pass

def _unofficial_age_lookup(geo_age):
    try:
        return tuple(next(value for key, value in GEO_AGE_UNOFFICIAL.items() if key == geo_age))
    except StopIteration:
        pass

def geologic_age(age):
    """
    Given a numeric age, will return a stratigraphic age. If a list is given, will return the most accurate stratigraphic age that encompasses all values in the list. Returns None if incorrect type exists in the list.
    """
    def geo_age_inner(age):
        geo_age = OrderedDict()

        for k, v in GEO_AGE.items():
            try:
                geo_age[k] = _age_lookup(age,v)
            except StopIteration:
                geo_age[k] = ''
        return geo_age

    if isinstance(age,list):
        try:
            age_min = geo_age_inner(min(age))
            age_max = geo_age_inner(max(age))
            return OrderedDict((k,v) for k,v in age_min.items() if age_min[k] == age_max[k])
        except TypeError:
            return None

    else:
        return geo_age_inner(age)

def age_range(geo_age):

    geo_age = '-'.join(geo_age.split(' ')).lower()

    # convert stratigraphic age to geochronological age
    for i in [('lower','early'),('upper','late'),('palaeo','paleo')]:
        if i[0] in geo_age:
            geo_age = geo_age.replace(i[0],i[1])


    # loop through GEO_AGE dictionary and try to find a match
    found = _geo_age_lookup(geo_age)

    # search unofficial age names for a match
    if not found:
        found = _unofficial_age_lookup(geo_age)


    # if a match still can't be found, remove any prefixes and search by the end index to hopefully match a broader age
    if not found and '-' in geo_age:
        geo_age_new = geo_age.split('-')[1]
        # print('Warning: could not match {}, searching instead for {}'.format(geo_age,geo_age_new))
        found = _geo_age_lookup(geo_age_new)

        # once again try search unofficial names
        if not found:
            found = _unofficial_age_lookup(geo_age_new)

    
    return found



