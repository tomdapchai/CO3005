.source Queue.java
.class public Queue
.super java/lang/Object
.field items [I
.field front I
.field rear I

.method public <init>([III)V
.var 0 is this LQueue; from Label0 to Label1
.var 1 is items [I from Label0 to Label1
.var 2 is front I from Label0 to Label1
.var 3 is rear I from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
	aload_0
	aload_1
	putfield Queue/items [I
	aload_0
	iload_2
	putfield Queue/front I
	aload_0
	iload_3
	putfield Queue/rear I
Label1:
	return
.limit stack 2
.limit locals 4
.end method

.method public <init>()V
.var 0 is this LQueue; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public initialize()LQueue;
.var 0 is this LQueue; from Label0 to Label1
Label0:
Label2:
	aload_0
	iconst_0
	putfield Queue/front I
	aload_0
	iconst_1
	ineg
	putfield Queue/rear I
	aload_0
	iconst_5
	newarray int
	dup
	iconst_0
	iconst_0
	iastore
	dup
	iconst_1
	iconst_0
	iastore
	dup
	iconst_2
	iconst_0
	iastore
	dup
	iconst_3
	iconst_0
	iastore
	dup
	iconst_4
	iconst_0
	iastore
	putfield Queue/items [I
	aload_0
	areturn
Label3:
Label1:
.limit stack 12
.limit locals 1
.end method

.method public enqueue(I)LQueue;
.var 0 is this LQueue; from Label0 to Label1
Label0:
.var 1 is item I from Label0 to Label1
Label2:
	aload_0
	getfield Queue/rear I
	iconst_4
	if_icmpge Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label4
Label8:
	aload_0
	aload_0
	getfield Queue/rear I
	iconst_1
	iadd
	putfield Queue/rear I
	aload_0
	getfield Queue/items [I
	aload_0
	getfield Queue/rear I
	iload_1
	iastore
Label9:
Label4:
	aload_0
	areturn
Label3:
Label1:
.limit stack 8
.limit locals 2
.end method

.method public dequeue()I
.var 0 is this LQueue; from Label0 to Label1
Label0:
Label2:
	aload_0
	getfield Queue/front I
	aload_0
	getfield Queue/rear I
	if_icmpgt Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label4
Label8:
	aload_0
	getfield Queue/items [I
	aload_0
	getfield Queue/front I
	iaload
.var 1 is item I from Label8 to Label9
	istore_1
	aload_0
	aload_0
	getfield Queue/front I
	iconst_1
	iadd
	putfield Queue/front I
	iload_1
	ireturn
Label9:
Label4:
	iconst_1
	ineg
	ireturn
Label3:
Label1:
.limit stack 6
.limit locals 2
.end method

.method public display()V
.var 0 is this LQueue; from Label0 to Label1
Label0:
Label2:
	aload_0
	getfield Queue/front I
.var 1 is i I from Label2 to Label3
	istore_1
Label6:
	iload_1
	aload_0
	getfield Queue/rear I
	if_icmpgt Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifle Label5
Label9:
	aload_0
	getfield Queue/items [I
	iload_1
	iaload
	invokestatic io/putIntLn(I)V
Label10:
Label4:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label6
Label5:
Label3:
Label1:
	return
.limit stack 5
.limit locals 2
.end method
