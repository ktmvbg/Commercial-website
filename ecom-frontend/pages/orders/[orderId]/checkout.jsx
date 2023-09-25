import Head from 'next/head'
import Image from 'next/image'
import NormalLayout from 'components/layouts/NormalLayout'
import Checkout from 'components/Checkout/Checkout'

export default function CheckoutPage() {
    return (
        <Checkout />
    )
}


CheckoutPage.getLayout = function getLayout(page) {
    return (
        <NormalLayout>
            {page}
        </NormalLayout>
    )
}