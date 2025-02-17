import re

def WordCount(sentences:str):
    count=0
    WCount={}
    words=re.split(r"[ .,:;')(?!]+",sentences.lower())
    for word in words :
    
        for w in words:
            if word==w:
                count+=1
        if word not in WCount.keys():
            WCount[word]=count
            words=[w for w in words if w!=word]
            count=0
    return WCount


if __name__=="__main__":
    sentences="""Le Sénégal, qui se lit en wolof "Réewum Senegaal", en forme longue la république du Sénégal, est un État d'Afrique de l'Ouest.
Il est bordé par l'océan Atlantique à l'ouest, la Mauritanie au nord-nord-est, le Mali à l'est-sud-est, la Guinée au sud-est et la Guinée-Bissau au sud-sud-ouest. La Gambie forme une quasi-enclave dans le Sénégal, pénétrant à plus de 302 km à l'intérieur des terres. Les îles du Cap-Vert sont situées à 560 km de la côte sénégalaise.
Le pays doit son nom au fleuve qui le borde à l'est et au nord et qui prend sa source dans le Fouta-Djalon en Guinée. Le climat est tropical et sec avec deux saisons : la saison sèche et la saison des pluies.
Le Sénégal fait partie de la Communauté économique des États de l'Afrique de l'Ouest (CEDEAO). Intégré aux principales instances de la communauté internationale, le Sénégal fait également partie de l'Union africaine (UA), de la Communauté des États sahélo-sahariens (CES), de l'Organisation internationale de la francophonie et de l'Organisation de la coopération islamique.
Depuis le 2 avril 2012, le président du pays est Macky Sall."""
    getListe = WordCount(sentences)
    for key,value in getListe.items():
        print(f"{key}: {value}")