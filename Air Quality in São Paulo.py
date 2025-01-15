# Objetivo: Identificar a variação de dióxido de nitrogênio (µg/m³) presente no ar do Estado de São Paulo ao longo do dia.

# Importando as Bibliotecas.
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime

# Importando o DataFrame do Kaggle e realizando uma Análise Exploratória dos dados.
air_quality = pd.read_csv('sp_air_quality.csv')
print(air_quality.head(3))

# Criando a coluna 'Hour' a partir da coluna 'Datetime'.
air_quality['Datetime'] = pd.to_datetime(air_quality['Datetime'])
air_quality['Hour'] = air_quality['Datetime'].dt.hour

# Replicando os valores únicos da coluna 'Station' para uma nova lista.
stations = {
    'Station':['Araçatuba', 'Catanduva', 'Pico do Jaraguá', 'Ribeirão Preto','Araraquara', 'São José do Rio Preto', 
'Bauru', 'Jaú', 'Jundiaí', 'Marília', 'Paulínia', 'Piracicaba', 'Sorocaba', 'Tatuí', 'Campinas-Centro', 'Campinas-V.União', 'Campinas-Taquaral',
'Americana','Limeira','Santa Gertrudes', 'Carapicuíba', 'Diadema', 'Guarulhos-Paço Municipal', 'Guarulhos-Pimentas', 
'Mauá', 'Osasco', 'Perus', 'S.André-Capuava', 'S.Bernardo-Centro', 'S.Bernardo-Paulicéia', 'São Caetano do Sul', 'Taboão da Serra',
'Guaratinguetá', 'Jacareí', 'S.José Campos', 'S.José Campos-Jd.Satelite', 'S.José Campos-Vista Verde', 'Taubaté',
'Capão Redondo', 'Congonhas', 'Grajaú-Parelheiros', 'Interlagos', 'Santo Amaro', 'Cubatão-Centro', 'Cubatão-V.Parisi', 'Cubatão-Vale do Mogi', 
'Santos', 'Santos-Ponta da Praia', 'Cerqueira César', 'Ibirapuera', 'Marg.Tietê-Pte Remédios', 'Parque D.Pedro II', 'Rio Claro-Jd.Guanabara',
'N.Senhora do Ó', 'Santana', 'Itaim Paulista', 'Itaquera', 'Mooca']
}

# Transformando a lista em um novo DataFrame
region_list =pd.DataFrame(stations)

# Criando uma nova lista designando os bairros presentes no DataFrame as suas respectivas regiões.
region =  {
    'Interior': ['Bauru', 'Jaú', 'Jundiaí', 'Marília', 'Paulínia', 'Piracicaba', 'Sorocaba', 'Tatuí', 'Araraquara', 'São José do Rio Preto','Araçatuba', 'Catanduva', 'Pico do Jaraguá', 'Ribeirão Preto'], 
    'Campinas': ['Campinas-Centro', 'Campinas-V.União', 'Campinas-Taquaral','Americana','Limeira','Santa Gertrudes'], 
    'Grande SP': ['Carapicuíba', 'Diadema', 'Guarulhos-Paço Municipal', 'Guarulhos-Pimentas', 'Mauá', 'Osasco', 'Perus', 'S.André-Capuava', 'S.Bernardo-Centro', 'S.Bernardo-Paulicéia', 'São Caetano do Sul', 'Taboão da Serra'], 
    'Vale do Paraíba': ['Guaratinguetá', 'Jacareí', 'S.José Campos', 'S.José Campos-Jd.Satelite', 'S.José Campos-Vista Verde', 'Taubaté'], 
    'Litoral': ['Cubatão-Centro', 'Cubatão-V.Parisi', 'Cubatão-Vale do Mogi', 'Santos', 'Santos-Ponta da Praia'], 
    'SP Capital': ['Cerqueira César', 'Ibirapuera', 'Marg.Tietê-Pte Remédios', 'Parque D.Pedro II', 'Rio Claro-Jd.Guanabara','N.Senhora do Ó', 'Santana','Itaim Paulista', 'Itaquera', 'Mooca', 'Capão Redondo', 'Congonhas', 'Grajaú-Parelheiros', 'Interlagos', 'Santo Amaro']
}

# Criando a coluna 'Region' no DataFrame 'region_list'.
station_to_region = {station: reg for reg, stations in region.items() for station in stations}
region_list['Region'] = region_list['Station'].map(station_to_region)

# Realizando uma junção à esquerda para que a coluna 'Region' de 'region_list' seja adicionada no DataFrame 'air_quality'.
air_quality_merge = air_quality.merge(region_list, how='left', on='Station')

# Identificando quais regiões têm a maior média de concentração de dióxido de nitrogênio.
NO2_mean_per_region = air_quality_merge.groupby('Region')['NO2'].mean()
print(NO2_mean_per_region)

# Criando o gráfico da variação de NO2 por hora para cada região do Estado de São Paulo.
sns.set_context('paper')
a = sns.relplot(x='Hour', y='NO2', data=air_quality_merge, kind='line', hue='Region')
a.fig.suptitle('NO2 (µg/m³) per hour in São Paulo')
a.set(xlabel= 'Hour', ylabel='Nitrogen dioxide (µg/m³)')
plt.xticks([00,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23],)
plt.show()

# Conclusão:

# 1.Padrão Diurno/Noturno
#   1.1. Observa-se um pico de concentração de NO2, geralmente entre 6h e 10h, que coincide com o maior tráfego no período matutino.
#   1.2. O segundo pico significativo ocorre entre 17h e 20h, também relacionado ao tráfego intenso mo horário de pico vespertino.
#   1.3. Durante o horário da madrugada (1h e 5h) e no início da tarde (11h a 15h), as concentrações de NO₂ são as mais baixas, refletindo menor atividade veicular e dispersão dos poluentes devido ao aumento da temperatura e da radiação solar.

# 2.Diferença entre as regiões.
#   2.1 As regiões de SP Capital), Grande SP e Litoral apresentam as maiores concentrações de NO₂ ao longo do dia, o que pode ser explicado pela maior densidade populacional, tráfego intenso e atividades industriais.
#   2.2 As regiões do Vale do Paraíba e Interior apresentam as menores concentrações de NO₂ ao longo do dia, o que pode ser explicado pela menor densidade populacional e menor atividade industrial.
