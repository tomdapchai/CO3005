.source Outr.java
.class public Outr
.super java/lang/Object
.field name Ljava/lang/String;
.field innr LInnr;

.method public <init>(Ljava/lang/String;LInnr;)V
.var 0 is this LOutr; from Label0 to Label1
.var 1 is name Ljava/lang/String; from Label0 to Label1
.var 2 is innr LInnr; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
	aload_0
	aload_1
	putfield Outr/name Ljava/lang/String;
	aload_0
	aload_2
	putfield Outr/innr LInnr;
Label1:
	return
.limit stack 2
.limit locals 3
.end method

.method public <init>()V
.var 0 is this LOutr; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method
