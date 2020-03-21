__all__ = ['eng2kor']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['JUNG_DATA', 'JONG_DATA', 'engTypeToKor', 'CHO_DATA', 'korTypeToEng', 'KOR_KEY', 'ENG_KEY', 'makeHangul'])
@Js
def PyJsHoisted_engTypeToKor_(r, this, arguments, var=var):
    var = Scope({'r':r, 'this':this, 'arguments':arguments}, var)
    var.registers(['o', 'i', 'q', 'n', 'l', 'r', 'k', 'm', 'p'])
    var.put('l', Js(''))
    if (var.get('r').get('length')==Js(0.0)):
        return var.get('l')
    var.put('i', (-Js(1.0)))
    var.put('k', (-Js(1.0)))
    var.put('m', (-Js(1.0)))
    #for JS loop
    var.put('o', Js(0.0))
    while (var.get('o')<var.get('r').get('length')):
        try:
            var.put('q', var.get('r').callprop('charAt', var.get('o')))
            var.put('p', var.get('ENG_KEY').callprop('indexOf', var.get('q')))
            if (var.get('p')==(-Js(1.0))):
                var.put('p', var.get('ENG_KEY').callprop('indexOf', var.get('q').callprop('toLowerCase')))
            if (var.get('p')==(-Js(1.0))):
                if (var.get('i')!=(-Js(1.0))):
                    if (var.get('k')!=(-Js(1.0))):
                        var.put('l', var.get('makeHangul')(var.get('i'), var.get('k'), var.get('m')), '+')
                    else:
                        var.put('l', var.get('CHO_DATA').callprop('charAt', var.get('i')), '+')
                else:
                    if (var.get('k')!=(-Js(1.0))):
                        var.put('l', var.get('JUNG_DATA').callprop('charAt', var.get('k')), '+')
                    else:
                        if (var.get('m')!=(-Js(1.0))):
                            var.put('l', var.get('JONG_DATA').callprop('charAt', var.get('m')), '+')
                var.put('i', (-Js(1.0)))
                var.put('k', (-Js(1.0)))
                var.put('m', (-Js(1.0)))
                var.put('l', var.get('q'), '+')
            else:
                if (var.get('p')<Js(19.0)):
                    if (var.get('k')!=(-Js(1.0))):
                        if (var.get('i')==(-Js(1.0))):
                            var.put('l', var.get('JUNG_DATA').callprop('charAt', var.get('k')), '+')
                            var.put('k', (-Js(1.0)))
                            var.put('i', var.get('CHO_DATA').callprop('indexOf', var.get('KOR_KEY').callprop('charAt', var.get('p'))))
                        else:
                            if (var.get('m')==(-Js(1.0))):
                                var.put('m', var.get('JONG_DATA').callprop('indexOf', var.get('KOR_KEY').callprop('charAt', var.get('p'))))
                                if (var.get('m')==(-Js(1.0))):
                                    var.put('l', var.get('makeHangul')(var.get('i'), var.get('k'), var.get('m')), '+')
                                    var.put('i', var.get('CHO_DATA').callprop('indexOf', var.get('KOR_KEY').callprop('charAt', var.get('p'))))
                                    var.put('k', (-Js(1.0)))
                            else:
                                if ((var.get('m')==Js(0.0)) and (var.get('p')==Js(9.0))):
                                    var.put('m', Js(2.0))
                                else:
                                    if ((var.get('m')==Js(3.0)) and (var.get('p')==Js(12.0))):
                                        var.put('m', Js(4.0))
                                    else:
                                        if ((var.get('m')==Js(3.0)) and (var.get('p')==Js(18.0))):
                                            var.put('m', Js(5.0))
                                        else:
                                            if ((var.get('m')==Js(7.0)) and (var.get('p')==Js(0.0))):
                                                var.put('m', Js(8.0))
                                            else:
                                                if ((var.get('m')==Js(7.0)) and (var.get('p')==Js(6.0))):
                                                    var.put('m', Js(9.0))
                                                else:
                                                    if ((var.get('m')==Js(7.0)) and (var.get('p')==Js(7.0))):
                                                        var.put('m', Js(10.0))
                                                    else:
                                                        if ((var.get('m')==Js(7.0)) and (var.get('p')==Js(9.0))):
                                                            var.put('m', Js(11.0))
                                                        else:
                                                            if ((var.get('m')==Js(7.0)) and (var.get('p')==Js(16.0))):
                                                                var.put('m', Js(12.0))
                                                            else:
                                                                if ((var.get('m')==Js(7.0)) and (var.get('p')==Js(17.0))):
                                                                    var.put('m', Js(13.0))
                                                                else:
                                                                    if ((var.get('m')==Js(7.0)) and (var.get('p')==Js(18.0))):
                                                                        var.put('m', Js(14.0))
                                                                    else:
                                                                        if ((var.get('m')==Js(16.0)) and (var.get('p')==Js(9.0))):
                                                                            var.put('m', Js(17.0))
                                                                        else:
                                                                            var.put('l', var.get('makeHangul')(var.get('i'), var.get('k'), var.get('m')), '+')
                                                                            var.put('i', var.get('CHO_DATA').callprop('indexOf', var.get('KOR_KEY').callprop('charAt', var.get('p'))))
                                                                            var.put('k', (-Js(1.0)))
                                                                            var.put('m', (-Js(1.0)))
                    else:
                        if (var.get('i')==(-Js(1.0))):
                            if (var.get('m')!=(-Js(1.0))):
                                var.put('l', var.get('JONG_DATA').callprop('charAt', var.get('m')), '+')
                                var.put('m', (-Js(1.0)))
                            var.put('i', var.get('CHO_DATA').callprop('indexOf', var.get('KOR_KEY').callprop('charAt', var.get('p'))))
                        else:
                            if ((var.get('i')==Js(0.0)) and (var.get('p')==Js(9.0))):
                                var.put('i', (-Js(1.0)))
                                var.put('m', Js(2.0))
                            else:
                                if ((var.get('i')==Js(2.0)) and (var.get('p')==Js(12.0))):
                                    var.put('i', (-Js(1.0)))
                                    var.put('m', Js(4.0))
                                else:
                                    if ((var.get('i')==Js(2.0)) and (var.get('p')==Js(18.0))):
                                        var.put('i', (-Js(1.0)))
                                        var.put('m', Js(5.0))
                                    else:
                                        if ((var.get('i')==Js(5.0)) and (var.get('p')==Js(0.0))):
                                            var.put('i', (-Js(1.0)))
                                            var.put('m', Js(8.0))
                                        else:
                                            if ((var.get('i')==Js(5.0)) and (var.get('p')==Js(6.0))):
                                                var.put('i', (-Js(1.0)))
                                                var.put('m', Js(9.0))
                                            else:
                                                if ((var.get('i')==Js(5.0)) and (var.get('p')==Js(7.0))):
                                                    var.put('i', (-Js(1.0)))
                                                    var.put('m', Js(10.0))
                                                else:
                                                    if ((var.get('i')==Js(5.0)) and (var.get('p')==Js(9.0))):
                                                        var.put('i', (-Js(1.0)))
                                                        var.put('m', Js(11.0))
                                                    else:
                                                        if ((var.get('i')==Js(5.0)) and (var.get('p')==Js(16.0))):
                                                            var.put('i', (-Js(1.0)))
                                                            var.put('m', Js(12.0))
                                                        else:
                                                            if ((var.get('i')==Js(5.0)) and (var.get('p')==Js(17.0))):
                                                                var.put('i', (-Js(1.0)))
                                                                var.put('m', Js(13.0))
                                                            else:
                                                                if ((var.get('i')==Js(5.0)) and (var.get('p')==Js(18.0))):
                                                                    var.put('i', (-Js(1.0)))
                                                                    var.put('m', Js(14.0))
                                                                else:
                                                                    if ((var.get('i')==Js(7.0)) and (var.get('p')==Js(9.0))):
                                                                        var.put('i', (-Js(1.0)))
                                                                        var.put('m', Js(17.0))
                                                                    else:
                                                                        var.put('l', var.get('CHO_DATA').callprop('charAt', var.get('i')), '+')
                                                                        var.put('i', var.get('CHO_DATA').callprop('indexOf', var.get('KOR_KEY').callprop('charAt', var.get('p'))))
                else:
                    if (var.get('m')!=(-Js(1.0))):
                        pass
                        if (var.get('m')==Js(2.0)):
                            var.put('m', Js(0.0))
                            var.put('n', Js(9.0))
                        else:
                            if (var.get('m')==Js(4.0)):
                                var.put('m', Js(3.0))
                                var.put('n', Js(12.0))
                            else:
                                if (var.get('m')==Js(5.0)):
                                    var.put('m', Js(3.0))
                                    var.put('n', Js(18.0))
                                else:
                                    if (var.get('m')==Js(8.0)):
                                        var.put('m', Js(7.0))
                                        var.put('n', Js(0.0))
                                    else:
                                        if (var.get('m')==Js(9.0)):
                                            var.put('m', Js(7.0))
                                            var.put('n', Js(6.0))
                                        else:
                                            if (var.get('m')==Js(10.0)):
                                                var.put('m', Js(7.0))
                                                var.put('n', Js(7.0))
                                            else:
                                                if (var.get('m')==Js(11.0)):
                                                    var.put('m', Js(7.0))
                                                    var.put('n', Js(9.0))
                                                else:
                                                    if (var.get('m')==Js(12.0)):
                                                        var.put('m', Js(7.0))
                                                        var.put('n', Js(16.0))
                                                    else:
                                                        if (var.get('m')==Js(13.0)):
                                                            var.put('m', Js(7.0))
                                                            var.put('n', Js(17.0))
                                                        else:
                                                            if (var.get('m')==Js(14.0)):
                                                                var.put('m', Js(7.0))
                                                                var.put('n', Js(18.0))
                                                            else:
                                                                if (var.get('m')==Js(17.0)):
                                                                    var.put('m', Js(16.0))
                                                                    var.put('n', Js(9.0))
                                                                else:
                                                                    var.put('n', var.get('CHO_DATA').callprop('indexOf', var.get('JONG_DATA').callprop('charAt', var.get('m'))))
                                                                    var.put('m', (-Js(1.0)))
                        if (var.get('i')!=(-Js(1.0))):
                            var.put('l', var.get('makeHangul')(var.get('i'), var.get('k'), var.get('m')), '+')
                        else:
                            var.put('l', var.get('JONG_DATA').callprop('charAt', var.get('m')), '+')
                        var.put('i', var.get('n'))
                        var.put('k', (-Js(1.0)))
                        var.put('m', (-Js(1.0)))
                    if (var.get('k')==(-Js(1.0))):
                        var.put('k', var.get('JUNG_DATA').callprop('indexOf', var.get('KOR_KEY').callprop('charAt', var.get('p'))))
                    else:
                        if ((var.get('k')==Js(8.0)) and (var.get('p')==Js(19.0))):
                            var.put('k', Js(9.0))
                        else:
                            if ((var.get('k')==Js(8.0)) and (var.get('p')==Js(20.0))):
                                var.put('k', Js(10.0))
                            else:
                                if ((var.get('k')==Js(8.0)) and (var.get('p')==Js(32.0))):
                                    var.put('k', Js(11.0))
                                else:
                                    if ((var.get('k')==Js(13.0)) and (var.get('p')==Js(23.0))):
                                        var.put('k', Js(14.0))
                                    else:
                                        if ((var.get('k')==Js(13.0)) and (var.get('p')==Js(24.0))):
                                            var.put('k', Js(15.0))
                                        else:
                                            if ((var.get('k')==Js(13.0)) and (var.get('p')==Js(32.0))):
                                                var.put('k', Js(16.0))
                                            else:
                                                if ((var.get('k')==Js(18.0)) and (var.get('p')==Js(32.0))):
                                                    var.put('k', Js(19.0))
                                                else:
                                                    if (var.get('i')!=(-Js(1.0))):
                                                        var.put('l', var.get('makeHangul')(var.get('i'), var.get('k'), var.get('m')), '+')
                                                        var.put('i', (-Js(1.0)))
                                                    else:
                                                        var.put('l', var.get('JUNG_DATA').callprop('charAt', var.get('k')), '+')
                                                    var.put('k', (-Js(1.0)))
                                                    var.put('l', var.get('KOR_KEY').callprop('charAt', var.get('p')), '+')
        finally:
                (var.put('o',Js(var.get('o').to_number())+Js(1))-Js(1))
    if (var.get('i')!=(-Js(1.0))):
        if (var.get('k')!=(-Js(1.0))):
            var.put('l', var.get('makeHangul')(var.get('i'), var.get('k'), var.get('m')), '+')
        else:
            var.put('l', var.get('CHO_DATA').callprop('charAt', var.get('i')), '+')
    else:
        if (var.get('k')!=(-Js(1.0))):
            var.put('l', var.get('JUNG_DATA').callprop('charAt', var.get('k')), '+')
        else:
            if (var.get('m')!=(-Js(1.0))):
                var.put('l', var.get('JONG_DATA').callprop('charAt', var.get('m')), '+')
    return var.get('l')
PyJsHoisted_engTypeToKor_.func_name = 'engTypeToKor'
var.put('engTypeToKor', PyJsHoisted_engTypeToKor_)
@Js
def PyJsHoisted_makeHangul_(d, f, e, this, arguments, var=var):
    var = Scope({'d':d, 'f':f, 'e':e, 'this':this, 'arguments':arguments}, var)
    var.registers(['f', 'd', 'e'])
    return var.get('String').callprop('fromCharCode', ((((Js(44032.0)+((var.get('d')*Js(21.0))*Js(28.0)))+(var.get('f')*Js(28.0)))+var.get('e'))+Js(1.0)))
PyJsHoisted_makeHangul_.func_name = 'makeHangul'
var.put('makeHangul', PyJsHoisted_makeHangul_)
@Js
def PyJsHoisted_korTypeToEng_(t, this, arguments, var=var):
    var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
    var.registers(['o', 'm', 'i', 'q', 't', 'r', 'j', 'n', 's', 'p'])
    var.put('n', Js(''))
    if (var.get('t').get('length')==Js(0.0)):
        return var.get('n')
    #for JS loop
    var.put('q', Js(0.0))
    while (var.get('q')<var.get('t').get('length')):
        try:
            var.put('s', var.get('t').callprop('charAt', var.get('q')))
            var.put('i', var.get('s').callprop('charCodeAt', Js(0.0)))
            var.put('j', var.get('CHO_DATA').callprop('indexOf', var.get('s')))
            var.put('m', var.get('JUNG_DATA').callprop('indexOf', var.get('s')))
            var.put('o', var.get('JONG_DATA').callprop('indexOf', var.get('s')))
            var.put('p', Js([(-Js(1.0)), (-Js(1.0)), (-Js(1.0)), (-Js(1.0)), (-Js(1.0))]))
            if ((Js(44032.0)<=var.get('i')) and (var.get('i')<=Js(55203.0))):
                var.put('i', Js(44032.0), '-')
                var.get('p').put('0', var.get('Math').callprop('floor', (var.get('i')/(Js(21.0)*Js(28.0)))))
                var.get('p').put('1', (var.get('Math').callprop('floor', (var.get('i')/Js(28.0)))%Js(21.0)))
                var.get('p').put('3', ((var.get('i')%Js(28.0))-Js(1.0)))
            else:
                if (var.get('j')!=(-Js(1.0))):
                    var.get('p').put('0', var.get('j'))
                else:
                    if (var.get('m')!=(-Js(1.0))):
                        var.get('p').put('1', var.get('m'))
                    else:
                        if (var.get('o')!=(-Js(1.0))):
                            var.get('p').put('3', var.get('o'))
                        else:
                            var.put('n', var.get('s'), '+')
            if (var.get('p').get('1')!=(-Js(1.0))):
                if (var.get('p').get('1')==Js(9.0)):
                    var.get('p').put('1', Js(27.0))
                    var.get('p').put('2', Js(19.0))
                else:
                    if (var.get('p').get('1')==Js(10.0)):
                        var.get('p').put('1', Js(27.0))
                        var.get('p').put('2', Js(20.0))
                    else:
                        if (var.get('p').get('1')==Js(11.0)):
                            var.get('p').put('1', Js(27.0))
                            var.get('p').put('2', Js(32.0))
                        else:
                            if (var.get('p').get('1')==Js(14.0)):
                                var.get('p').put('1', Js(29.0))
                                var.get('p').put('2', Js(23.0))
                            else:
                                if (var.get('p').get('1')==Js(15.0)):
                                    var.get('p').put('1', Js(29.0))
                                    var.get('p').put('2', Js(24.0))
                                else:
                                    if (var.get('p').get('1')==Js(16.0)):
                                        var.get('p').put('1', Js(29.0))
                                        var.get('p').put('2', Js(32.0))
                                    else:
                                        if (var.get('p').get('1')==Js(19.0)):
                                            var.get('p').put('1', Js(31.0))
                                            var.get('p').put('2', Js(32.0))
                                        else:
                                            var.get('p').put('1', var.get('KOR_KEY').callprop('indexOf', var.get('JUNG_DATA').callprop('charAt', var.get('p').get('1'))))
                                            var.get('p').put('2', (-Js(1.0)))
            if (var.get('p').get('3')!=(-Js(1.0))):
                if (var.get('p').get('3')==Js(2.0)):
                    var.get('p').put('3', Js(0.0))
                    var.get('p').put('4', Js(9.0))
                else:
                    if (var.get('p').get('3')==Js(4.0)):
                        var.get('p').put('3', Js(2.0))
                        var.get('p').put('4', Js(12.0))
                    else:
                        if (var.get('p').get('3')==Js(5.0)):
                            var.get('p').put('3', Js(2.0))
                            var.get('p').put('4', Js(18.0))
                        else:
                            if (var.get('p').get('3')==Js(8.0)):
                                var.get('p').put('3', Js(5.0))
                                var.get('p').put('4', Js(0.0))
                            else:
                                if (var.get('p').get('3')==Js(9.0)):
                                    var.get('p').put('3', Js(5.0))
                                    var.get('p').put('4', Js(6.0))
                                else:
                                    if (var.get('p').get('3')==Js(10.0)):
                                        var.get('p').put('3', Js(5.0))
                                        var.get('p').put('4', Js(7.0))
                                    else:
                                        if (var.get('p').get('3')==Js(11.0)):
                                            var.get('p').put('3', Js(5.0))
                                            var.get('p').put('4', Js(9.0))
                                        else:
                                            if (var.get('p').get('3')==Js(12.0)):
                                                var.get('p').put('3', Js(5.0))
                                                var.get('p').put('4', Js(16.0))
                                            else:
                                                if (var.get('p').get('3')==Js(13.0)):
                                                    var.get('p').put('3', Js(5.0))
                                                    var.get('p').put('4', Js(17.0))
                                                else:
                                                    if (var.get('p').get('3')==Js(14.0)):
                                                        var.get('p').put('3', Js(5.0))
                                                        var.get('p').put('4', Js(18.0))
                                                    else:
                                                        if (var.get('p').get('3')==Js(17.0)):
                                                            var.get('p').put('3', Js(7.0))
                                                            var.get('p').put('4', Js(9.0))
                                                        else:
                                                            var.get('p').put('3', var.get('KOR_KEY').callprop('indexOf', var.get('JONG_DATA').callprop('charAt', var.get('p').get('3'))))
                                                            var.get('p').put('4', (-Js(1.0)))
            #for JS loop
            var.put('r', Js(0.0))
            while (var.get('r')<Js(5.0)):
                try:
                    if (var.get('p').get(var.get('r'))!=(-Js(1.0))):
                        var.put('n', var.get('ENG_KEY').callprop('charAt', var.get('p').get(var.get('r'))), '+')
                finally:
                        (var.put('r',Js(var.get('r').to_number())+Js(1))-Js(1))
        finally:
                (var.put('q',Js(var.get('q').to_number())+Js(1))-Js(1))
    return var.get('n')
PyJsHoisted_korTypeToEng_.func_name = 'korTypeToEng'
var.put('korTypeToEng', PyJsHoisted_korTypeToEng_)
var.put('ENG_KEY', Js('rRseEfaqQtTdwWczxvgkoiOjpuPhynbml'))
var.put('KOR_KEY', Js('ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎㅏㅐㅑㅒㅓㅔㅕㅖㅗㅛㅜㅠㅡㅣ'))
var.put('CHO_DATA', Js('ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎ'))
var.put('JUNG_DATA', Js('ㅏㅐㅑㅒㅓㅔㅕㅖㅗㅘㅙㅚㅛㅜㅝㅞㅟㅠㅡㅢㅣ'))
var.put('JONG_DATA', Js('ㄱㄲㄳㄴㄵㄶㄷㄹㄺㄻㄼㄽㄾㄿㅀㅁㅂㅄㅅㅆㅇㅈㅊㅋㅌㅍㅎ'))



# Add lib to the module scope
eng2kor = var.to_python()