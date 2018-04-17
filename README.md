# Intelbrás TIP 100
## Reinicialização Remota

Script para reinicialização remota dos aparelhos TIP 100 da Intelbrás, pois presenciei problemas na utilização do mesmo em ambientes com Asterisk. 

### Problema

O principal problema que identificamos é: quando ocorre uma transferência assitida, B e C não conseguem se comunicar para passar informações, antes de conectar A e C. Segundo relatos do setor de engenharia da Intelbrás, reconhecendo o problema, ocorre uma falha na negociação dos *codecs* no ato da transferência.

O problema também ocorreu em outros ambientes, conforme pode-se observar nos *links* abaixo:
* http://listas.asteriskbrasil.org/pipermail/asteriskbrasil/2010-October/045114.html
* http://listas.asteriskbrasil.org/pipermail/asteriskbrasil/2010-October/045152.html
* http://listas.asteriskbrasil.org/pipermail/asteriskbrasil/2010-October/045185.html

### Solução (temporária)

A Intelbrás possui uma atualização de *firmware* do aparelho que, até o momento (abril de 2018), é *beta* e deveria resolver a situação, porém é compatível somente com os aparelhos TIP 100 (*excluindo-se os modelos PLIGG e LITE*). Tive relatos do cliente, que tem o cenário problemático, informando que melhorou bastante a situação, porém anda não resolvido completamente (*acreditamos que devido ao fato desse novo firwamre não ser compatível com o PLIGG e o LITE*).

Por mera observação, verificamos que após o aparelho ser reiniciado, o problema é mitigado por alguns dias. Para reduzir os impactos com o cliente, criamos um *script* para reiniciá-los remotamente, até que a Intelbrás venha a resolver o problema.
