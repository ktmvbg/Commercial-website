import Head from 'next/head'
import Image from 'next/image'
import NormalLayout from 'components/layouts/NormalLayout'
import Cart from 'components/Cart/Cart'

export default function CartPage() {
    return (
        <Cart />
    )
}


CartPage.getLayout = function getLayout(page) {
    return (
        <NormalLayout>
            {page}
        </NormalLayout>
    )
}