.source Person.java
.class public Person
.super java/lang/Object
.field age I
.field name Ljava/lang/String;
.field child [LChildren;

.method public <init>(ILjava/lang/String;[LChildren;)V
.var 0 is this LPerson; from Label0 to Label1
.var 1 is age I from Label0 to Label1
.var 2 is name Ljava/lang/String; from Label0 to Label1
.var 3 is child [LChildren; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
	aload_0
	iload_1
	putfield Person/age I
	aload_0
	aload_2
	putfield Person/name Ljava/lang/String;
	aload_0
	aload_3
	putfield Person/child [LChildren;
Label1:
	return
.limit stack 2
.limit locals 4
.end method

.method public <init>()V
.var 0 is this LPerson; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public getChild()V
.var 0 is this LPerson; from Label0 to Label1
Label0:
Label2:
	aload_0
	getfield Person/name Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
	aload_0
	getfield Person/age I
	invokestatic io/putIntLn(I)V
	iconst_0
.var 1 is i I from Label2 to Label3
	istore_1
Label6:
	iload_1
	getstatic MiniGoClass/childSize I
	if_icmpge Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifle Label5
Label9:
	aload_0
	getfield Person/child [LChildren;
	iload_1
	aaload
	getfield Children/name Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
	aload_0
	getfield Person/child [LChildren;
	iload_1
	aaload
	getfield Children/age I
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
.limit stack 6
.limit locals 2
.end method
