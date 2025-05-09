.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object
.field static childSize I = 2

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label2:
.var 1 is c [LChildren; from Label2 to Label3
	iconst_2
	anewarray Children
	dup
	iconst_0
	new Children
	dup
	iconst_5
	ldc "Hugo"
	invokespecial Children/<init>(ILjava/lang/String;)V
	aastore
	dup
	iconst_1
	new Children
	dup
	iconst_3
	ldc "Jerry"
	invokespecial Children/<init>(ILjava/lang/String;)V
	aastore
	astore_1
.var 2 is a LPerson; from Label2 to Label3
	new Person
	dup
	bipush 21
	ldc "Tom"
	aload_1
	invokespecial Person/<init>(ILjava/lang/String;[LChildren;)V
	astore_2
Label3:
Label1:
	return
.limit stack 10
.limit locals 3
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
