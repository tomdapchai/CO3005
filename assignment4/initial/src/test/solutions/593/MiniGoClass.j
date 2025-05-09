.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label2:
.var 1 is obj LOutr; from Label2 to Label3
	new Outr
	dup
	ldc "Hello"
	new Innr
	dup
	ldc "Bro"
	bipush 21
	invokespecial Innr/<init>(Ljava/lang/String;I)V
	invokespecial Outr/<init>(Ljava/lang/String;LInnr;)V
	astore_1
	aload_1
	getfield Outr/name Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
	aload_1
	getfield Outr/innr LInnr;
	getfield Innr/name Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label3:
Label1:
	return
.limit stack 8
.limit locals 2
.end method

.method public <init>()V
.var 0 is this LMiniGoClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static <clinit>()V
Label0:
Label1:
	return
.limit stack 0
.limit locals 0
.end method
