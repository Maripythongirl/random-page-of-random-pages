from flask import Flask
import random

app = Flask(__name__)
facts_list = [
    "Alterações no cérebro: Estudos indicam que o vício em internet pode provocar alterações estruturais e funcionais no cérebro de jovens (10 a 19 anos), afetando o desenvolvimento e comportamento. Áreas responsáveis pelo raciocínio e ponderação (lobo frontal) podem ser especialmente afetadas.",
    "A 'mágica' dopaminérgica: Jogos e redes sociais são projetados cientificamente para prender a atenção e ativar o sistema de recompensa do cérebro, liberando dopamina (prazer imediato), o que dificulta largar o celular.",
    "Sintomas de abstinência: Indivíduos com alto grau de dependência podem sentir irritabilidade, agressividade e ansiedade intensa quando privados de tecnologia.",
    "No Brasil, o uso excessivo de telas é comum, com pessoas passando mais de 9 horas por dia conectadas. Em Portugal, a média chega a 10 horas, superando o tempo médio de sono.",
    "Ficar offline também é importante 💙",
    "Uso diário seguro: Especialistas consideram o uso diário de tecnologia acima de 3 horas como excessivo, sendo o ideal cerca de 2 horas.",
    "Profissionais do Vale do Silício: É curioso notar que muitos criadores de tecnologia no Vale do Silício, EUA, restringem o uso de telas para seus próprios filhos, optando por escolas sem tecnologia no ensino fundamental.",
    "Meninas: Costumam ser mais afetadas pelas redes sociais, resultando em comparação, exclusão e ansiedade.",
    "Meninos: Tendem a desenvolver vício em videogames e pornografia, focando no prazer imediato."
]
coin_list = [
    "Cara🪙",
    "Coroa🪙"
]

meme_list = [
    "meme1.jpg",
    "meme2.jpg",
    "meme3.jpg",
    "meme4.jpg",
    "meme5.jpg",
    "meme6.jpg",
    "meme7.jpg",
    "meme8.jpg",
    "meme9.jpg",
    "meme10.jpg",
    "meme11.jpg",
    "meme12.jpg",
    "meme13.jpg",
    "meme14.jpg",
    "meme15.jpg",
    "meme16.jpg",
    "meme17.jpg"
]

#home
@app.route("/")
def home():
    return'''
    <h2> Bem-vindo visitante! Nesta página você pode encontrar outras páginas aleatórias!</h2>
    <br><br>
    <a href="/random_fact">Veja um fato aleatório!</a>
    <br><br>
    <a href="/coin">Jogar 'Cara ou Coroa'🪙</a>
    <br><br>
    <a href="/random_senha">Criar Senha Aleatória</a>
    <br><br>
    <a href="/animal_meme">🐾Ver meme de animal 🐾</a>
    '''
#pagina fato aleatorio
@app.route("/random_fact")
def random_fact():
    return f'''
    <h3>Curiosidades sobre Dependência Tecnológica</h3>
    <p>{random.choice(facts_list)}</p>
    <a href="/">Voltar</a>
    '''
#moeda
@app.route("/coin")
def coin():
    return f'''
    <h3>🪙Cara ou Coroa?🪙</h3>
    <p>{random.choice(coin_list)}</p>
    <a href="/">Voltar</a>
    '''

#senhas aleatórias
@app.route("/random_senha")
def senha():
    caracteres = " ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#"
    senha = "".join(random.choice(caracteres) for _ in range(8))
    return f'''
    <h3>Criação de uma Senha Aleatóris</h3>
    <h2>Sua senha:</h2>
    <p>{senha}</p>
    <a href='/'>Voltar</a>
    '''

#pagina meme animal
@app.route("/animal_meme")
def animal_meme():
    return f'''
    <h3>🐾Seu meme de animal é🐾:</h3>
    <img src="/static/{random.choice(meme_list)}" width="300">
    <br><br>
    <a href="/">Voltar</a>
    '''
app.run(debug=True)
