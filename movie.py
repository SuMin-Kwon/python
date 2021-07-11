# coding=utf-8
# 구글 > 영화순위 api > jp
box_office = {"boxOfficeResult":
    {"boxofficeType":"일별 박스오피스","showRange":"20210524~20210524","dailyBoxOfficeList":
        [
             {"rnum":"1","rank":"1","rankInten":"0","rankOldAndNew":"OLD","movieCd":"20205041",
             "movieNm":"분노의 질주: 더 얼티메이트","openDt":"2021-05-19","salesAmt":"668809180",
             "salesShare":"82.7","salesInten":"-1716348460","salesChange":"-72","salesAcc":"11759082780",
             "audiCnt":"71014","audiInten":"-169980","audiChange":"-70.5","audiAcc":"1203909","scrnCnt":"2030",
             "showCnt":"6730"},
             {"rnum":"2","rank":"2","rankInten":"1","rankOldAndNew":"OLD","movieCd":"20200703",
             "movieNm":"극장판 귀멸의 칼날: 무한열차편","openDt":"2021-01-27","salesAmt":"25559600",
             "salesShare":"3.2","salesInten":"-54517780","salesChange":"-68.1","salesAcc":"19723353460","audiCnt":"2678",
             "audiInten":"-5484","audiChange":"-67.2","audiAcc":"2047314","scrnCnt":"343","showCnt":"496"
             },
             {"rnum":"3","rank":"3","rankInten":"0","rankOldAndNew":"NEW","movieCd":"20194461","movieNm":"파이프라인",
              "openDt":"2021-05-26","salesAmt":"10033000","salesShare":"1.2","salesInten":"10033000","salesChange":"100",
              "salesAcc":"17974000","audiCnt":"1553","audiInten":"1553","audiChange":"100","audiAcc":"2750","scrnCnt":"9","showCnt":"10"
             },
             {"rnum":"4","rank":"4","rankInten":"0","rankOldAndNew":"OLD","movieCd":"20217484","movieNm":"스파이럴","openDt":"2021-05-12",
              "salesAmt":"14347620","salesShare":"1.8","salesInten":"-18055960","salesChange":"-55.7","salesAcc":"1234465230","audiCnt":"1448",
              "audiInten":"-1792","audiChange":"-55.3","audiAcc":"124297","scrnCnt":"338","showCnt":"446"
             },
             {"rnum":"5","rank":"5","rankInten":"1","rankOldAndNew":"OLD","movieCd":"20216703","movieNm":"더 스파이",
              "openDt":"2021-04-28","salesAmt":"9787210","salesShare":"1.2","salesInten":"-15463710","salesChange":"-61.2",
              "salesAcc":"2811463950","audiCnt":"1157","audiInten":"-1629","audiChange":"-58.5","audiAcc":"304428","scrnCnt":"238",
              "showCnt":"316"},{"rnum":"6","rank":"6","rankInten":"-4","rankOldAndNew":"OLD","movieCd":"20217478",
              "movieNm":"도라에몽: 스탠바이미 2","openDt":"2021-05-19","salesAmt":"9306010","salesShare":"1.2",
              "salesInten":"-104016330","salesChange":"-91.8","salesAcc":"528472760","audiCnt":"1073","audiInten":"-11736",
              "audiChange":"-91.6","audiAcc":"60401","scrnCnt":"290","showCnt":"357"
             },
             {"rnum":"7","rank":"7","rankInten":"0","rankOldAndNew":"OLD","movieCd":"20193068","movieNm":"비와 당신의 이야기",
              "openDt":"2021-04-28","salesAmt":"9122060","salesShare":"1.1","salesInten":"-12435500","salesChange":"-57.7",
              "salesAcc":"3384912840","audiCnt":"976","audiInten":"-1232","audiChange":"-55.8","audiAcc":"366297","scrnCnt":"234","showCnt":"318"
             },
             {"rnum":"8","rank":"8","rankInten":"1","rankOldAndNew":"OLD","movieCd":"20200295","movieNm":"혼자 사는 사람들",
              "openDt":"2021-05-19","salesAmt":"5644790","salesShare":"0.7","salesInten":"-6650590","salesChange":"-54.1",
              "salesAcc":"73293880","audiCnt":"649","audiInten":"-687","audiChange":"-51.4","audiAcc":"8090","scrnCnt":"135","showCnt":"190"
             },
             {"rnum":"9","rank":"9","rankInten":"1","rankOldAndNew":"OLD","movieCd":"20205144","movieNm":"미나리","openDt":"2021-03-03",
              "salesAmt":"4813970","salesShare":"0.6","salesInten":"-7064280","salesChange":"-59.5","salesAcc":"10153635200",
              "audiCnt":"581","audiInten":"-746","audiChange":"-56.2","audiAcc":"1125790","scrnCnt":"142","showCnt":"169"
             },
             {"rnum":"10","rank":"10","rankInten":"2","rankOldAndNew":"OLD","movieCd":"20194501","movieNm":"내일의 기억",
              "openDt":"2021-04-21","salesAmt":"4776000","salesShare":"0.6","salesInten":"-3799480","salesChange":"-44.3",
              "salesAcc":"3017263750","audiCnt":"475","audiInten":"-367","audiChange":"-43.6","audiAcc":"332095","scrnCnt":"115","showCnt":"157"
             }
        ]
    }
}
boxOfficeResult = box_office["boxOfficeResult"]
movie_list = boxOfficeResult["dailyBoxOfficeList"]
for dic in movie_list :
    print(dic["rank"],"위",dic["movieNm"])

