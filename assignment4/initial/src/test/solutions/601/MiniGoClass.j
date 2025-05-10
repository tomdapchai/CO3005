.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label2:
.var 1 is people [LSpeaker; from Label2 to Label3
	iconst_3
	anewarray Speaker
	astore_1
.var 2 is a I from Label2 to Label3
	iconst_1
	istore_2
.var 3 is b I from Label2 to Label3
	iconst_2
	istore_3
	aload_1
	iconst_0
	new Human
	dup
	iconst_1
	invokespecial Human/<init>(I)V
	aastore
	aload_1
	iload_3
	iload_2
	isub
	new Human
	dup
	iconst_2
	invokespecial Human/<init>(I)V
	aastore
	aload_1
	iconst_2
	new Human
	dup
	iconst_3
	invokespecial Human/<init>(I)V
	aastore
	aload_1
	iconst_0
	aaload
	invokeinterface Speaker/speak()V 1
	aload_1
	iconst_1
	aaload
	invokeinterface Speaker/speak()V 1
	aload_1
	iconst_2
	aaload
	invokeinterface Speaker/speak()V 1
Label3:
Label1:
	return
.limit stack 15
.limit locals 4
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
