.source HashTable.java
.class public HashTable
.super java/lang/Object
.field size I
.field table [I

.method public <init>(I[I)V
.var 0 is this LHashTable; from Label0 to Label1
.var 1 is size I from Label0 to Label1
.var 2 is table [I from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
	aload_0
	iload_1
	putfield HashTable/size I
	aload_0
	aload_2
	putfield HashTable/table [I
Label1:
	return
.limit stack 2
.limit locals 3
.end method

.method public <init>()V
.var 0 is this LHashTable; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public hash(I)I
.var 0 is this LHashTable; from Label0 to Label1
Label0:
.var 1 is key I from Label0 to Label1
Label2:
	iload_1
	aload_0
	getfield HashTable/size I
	irem
	ireturn
Label3:
Label1:
.limit stack 2
.limit locals 2
.end method
