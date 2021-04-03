
mianbiwi(chotekhan,chotirani).
mianbiwi(barrekhan,barrirani).
mianbiwi(salim,kauser).
mianbiwi(nadir,nahid).
mianbiwi(asad,sumra).
mianbiwi(rizwan,sanam).



parent(chotekhan,kauser).
parent(chotirani,kauser).
parent(chotekhan,nadir).
parent(chotirani,nadir).
parent(chotekhan,asad).
parent(chotirani,asad).
parent(barrekhan,nahid).
parent(barrirani,nahid).
parent(barrekhan,sumra).
parent(barrirani,sumra).
parent(salim,rizwan).
parent(kauser,rizwan).
parent(nadir,burhan).
parent(nahid,burhan).
parent(nadir,rashid).
parent(nahid,rashid).
parent(nadir,akram).
parent(nahid,akram).
parent(asad,salima).
parent(sumra,salima).
parent(asad,sanam).
parent(sumra,sanam).
parent(rizwan,rabia).
parent(sanam,rabia).




gins(male,chotekhan).
gins(male,barrekhan).
gins(male,salim).
gins(male,nadir).
gins(male,asad).
gins(male,rizwan).
gins(male,burhan).
gins(male,rashid).
gins(male,akram).



gins(female,chotirani).
gins(female,barrirani).
gins(female,kauser).
gins(female,nahid).
gins(female,sumra).
gins(female,salima).
gins(female,sanam).
gins(female,rabia).






beti(X,Y):-parent(Y,X) , gins(female,X).

beta(X,Y) :- parent(Y,X), gins(male,X).

dada(X,Y) :- parent(X,Z) , parent(Z,Y) , gins(male,X),gins(male,Z).

nana(X,Y) :- parent(X,Z), parent(Z,Y) , gins(male,X) , gins(female,Z).

dadi(X,Y) :- parent(X,Z),parent(Z,Y) , gins(female,X), gins(male,Z).

nani(X,Y) :- parent(X,Z),parent(Z,Y) , gins(female,X), gins(female,Z).

sala(X,Y) :- mianbiwi(Y,Z) , parent(A,Z) , gins(female,Z), parent(A,X) , gins(male,A), gins(male,X).

bahu(X,Y) :- parent(Y,Z) , gins(female,X) , gins(male,Z) , mianbiwi(Z,X).

pota(X,Y) :- parent(Y,Z), parent(Z,X) , gins(male,X),gins(male,Z).

nawasa(X,Y) :- parent(Y,Z), parent(Z,X) , gins(male,X), gins(female,Z).

sussar(X,Y) :- mianbiwi(Y,Z) , parent(X,Z) , gins(male,X), gins(female,Z), gins(male,Y).
sussar(X,Y) :- mianbiwi(Z,Y) , parent(X,Z) , gins(male,X), gins(male,Z), gins(female,Y).

baapDada(X,Y) :- parent(X,Y), gins(male,X).
baapDada(X,Y) :- parent(X,Z) ,baapDada(Z,Y),gins(male,Z),gins(male,X).

khala(X,Y) :- parent(Z,Y), gins(female,Z),parent(L,Y),gins(male,L),parent(A,Z), gins(male,A), parent(A,X), gins(female,X),not(mianbiwi(L,X)).

chachataya(X,Y) :- parent(Z,Y), gins(male,Z), parent(Ma,Y), gins(female,Ma), parent(A,Z), gins(male,A), parent(A,X), gins(male,X), not(mianbiwi(X,Ma)).
