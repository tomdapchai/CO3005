.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label2:
.var 1 is employees [LEmployee; from Label2 to Label3
	iconst_3
	anewarray Employee
	dup
	iconst_0
	new Employee
	dup
	ldc "Alice"
	bipush 101
	invokespecial Employee/<init>(Ljava/lang/String;I)V
	aastore
	dup
	iconst_1
	new Employee
	dup
	ldc "Bob"
	bipush 102
	invokespecial Employee/<init>(Ljava/lang/String;I)V
	aastore
	dup
	iconst_2
	new Employee
	dup
	ldc "Charlie"
	bipush 103
	invokespecial Employee/<init>(Ljava/lang/String;I)V
	aastore
	astore_1
	iconst_0
.var 2 is i I from Label2 to Label3
	istore_2
Label6:
	iload_2
	iconst_3
	if_icmpge Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifle Label5
Label9:
	ldc "Employee "
	aload_1
	iload_2
	aaload
	getfield Employee/name Ljava/lang/String;
	invokevirtual java/lang/String/concat(Ljava/lang/String;)Ljava/lang/String;
	ldc " has ID: "
	invokevirtual java/lang/String/concat(Ljava/lang/String;)Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
	aload_1
	iload_2
	aaload
	getfield Employee/id I
	invokestatic io/putIntLn(I)V
Label10:
Label4:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label6
Label5:
Label3:
Label1:
	return
.limit stack 11
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
