.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object
.field static a LIPerson;

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label2:
	getstatic MiniGoClass/a LIPerson;
	invokeinterface IPerson/bar()V 1
Label3:
Label1:
	return
.limit stack 1
.limit locals 1
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
	new Person
	dup
	ldc "John"
	bipush 30
	ldc 177.3
	invokespecial Person/<init>(Ljava/lang/String;IF)V
	putstatic MiniGoClass/a LIPerson;
Label1:
	return
.limit stack 6
.limit locals 0
.end method
